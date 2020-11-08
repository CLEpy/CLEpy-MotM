from diagrams import Diagram, Cluster, Edge
from diagrams.aws.analytics import ES
from diagrams.aws.compute import Lambda
from diagrams.aws.database import ElastiCache
from diagrams.aws.integration import SNS
from diagrams.aws.migration import TransferForSftp
from diagrams.aws.storage import S3
from diagrams.generic.os import Windows
from diagrams.k8s.compute import Job, Pod


def main():
    with Diagram('New SFTP Process') as diag:
        user = Windows('User')
        with Cluster('Repay-CDE-PROD-SFTP', direction='TB'):
            sftp_service = TransferForSftp('SFTP')
            s3_sftp_bucket = S3('channels_sftp_transfer')
            sftp_service - s3_sftp_bucket
            aws_sftp_group = [sftp_service, s3_sftp_bucket]

        user >> Edge(label='Upload a BLF into SFTP') >> sftp_service

        with Cluster('repay-cde-prod-channels', direction='TB'):
            lambda_blf_copy = Lambda('s3_copy_lambda')
            s3_blf_processor = S3('blf_processor bucket')
            sns_blf_uploaded_to_s3 = SNS('SNS - blf_uploaded_to_s3')
            redis = ElastiCache('(redis)')
            elasticsearch = ES('1 index per BLF')
            lambda_blf_copy >> s3_blf_processor
            s3_blf_processor >> sns_blf_uploaded_to_s3
            cde_group = [lambda_blf_copy, s3_blf_processor, sns_blf_uploaded_to_s3, redis, elasticsearch]

        with Cluster('repay-cde-prod-k8s', direction='TB'):
            k8s_api_pod = Pod('Channels API\n/api/v1/blf_upload_sns')
            k8s_blf_processor_job = Job('process-blf-k8s')
            k8s_api_pod >> Edge(label='Create job if no BLF lock exists for org/filename') >> k8s_blf_processor_job
            k8s_group = [k8s_api_pod, k8s_blf_processor_job]

        # TODO - MAKE SURE TO HIGHLIGHT THE USE OF INVISIBLE EDGES
        s3_sftp_bucket >> Edge(style='invis') >> cde_group
        redis >> Edge(style='invis') >> k8s_group
        elasticsearch >> Edge(style='invis') >> k8s_group

        k8s_blf_processor_job << Edge(label='Download file from s3') << s3_blf_processor
        s3_sftp_bucket >> Edge(label='S3 notification Object Created') >> lambda_blf_copy
        sns_blf_uploaded_to_s3 >> Edge(label='HTTP request with BLF file name') >> k8s_api_pod
        k8s_api_pod >> Edge(label='Create BLF lock - 5 minute expiration') >> redis
        k8s_blf_processor_job >> Edge(label='Delete BLF lock when done') >> redis
        k8s_blf_processor_job >> Edge(label='Create ES index') >> elasticsearch


if __name__ == '__main__':
    main()
