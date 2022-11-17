from google.cloud import storage
import os

cred=r'D:/Neodocs/serviceAccountKeyTesting.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = cred

storage_client = storage.Client(project='neodocs-test')
bucket = storage_client.bucket(bucket_name='neodocs-test.appspot.com')

local_path='D:\\Neodocs\\firebase images\\011022\\iphone8'

#don't start firebase folder path with a slash
firebase_folder_path='internal/mission14/LAB/011022/iPhone 8 Plus'

# Create a list of blobs object from the filepath
blobs=storage_client.list_blobs(bucket_or_name=bucket,prefix=firebase_folder_path)
for blob in blobs:
    print(f'{blob.name}')
    img_name=blob.name.split('/')[-1]
    # # Download the file to a destination
    blob.download_to_filename(f'{local_path}/{img_name}')




 # cred = credentials.Certificate("serviceAccountKeyTesting.json")
# Initialise a client

# storage_client = storage.Client("neodocs-test")
# # Create a bucket object for our bucket
# with open(r'D:/Neodocs/serviceAccountKeyTesting.json') as source:
#     info = json.load(source)
#
# storage_credentials = service_account.Credentials.from_service_account_info(info)
#  Initialize the app with a service account, granting admin privileges
# app = firebase_admin.initialize_app(cred, {
#     'storageBucket': 'neodocs-test.appspot.com',
# }, name='storage')