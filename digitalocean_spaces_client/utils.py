import boto3
from werkzeug.utils import secure_filename
import mimetypes
import os
import uuid
import urllib


def get_spaces_client(**kwargs):
    """
    Returns a DigitalOcean Spaces client.

    :param kwargs: A dictionary of keyword arguments.
    :keyword region_name: The name of the region where the DigitalOcean Space is located.
    :keyword endpoint_url: The URL endpoint for the DigitalOcean Space.
    :keyword key_id: The access key ID for the DigitalOcean Space.
    :keyword secret_access_key: The secret access key for the DigitalOcean Space.
    :return: A DigitalOcean Spaces client.
    """
    region_name = kwargs.get("region_name")
    endpoint_url = kwargs.get("endpoint_url")
    key_id = kwargs.get("key_id")
    secret_access_key = kwargs.get("secret_access_key")

    return boto3.client(
        's3',
        region_name=region_name,
        endpoint_url=endpoint_url,
        aws_access_key_id=key_id,
        aws_secret_access_key=secret_access_key
    )


def upload_file(spaces_client, space_name, file, is_public=True, region='nyc3') -> str:
    """
    Upload a file to DigitalOcean Spaces.

    :param spaces_client: The boto3 client for DigitalOcean Spaces, obtained from the `get_spaces_client` function.
    :param space_name: The unique name of the DigitalOcean Space to upload the file to.
    :param file: The file to be uploaded, represented as a byte array.
    :param is_public: If True, the file will be publicly accessible. If False, the file will be private. Defaults to True.
    :return: The URL of the uploaded file.

    This function uses the `spaces_client` to upload the `file` to the specified `space_name`. The content type of the file 
    is determined using the `mimetypes` library, or defaults to "application/octet-stream" if the content type cannot be 
    determined. A unique identifier for the file is generated using the `uuid` library. The uploaded file is given 
    the appropriate access level based on the `is_public` parameter. The URL of the uploaded file is returned.
    """
    file_name = secure_filename(file.filename)
    content_type = mimetypes.guess_type(file_name)[0]
    if content_type is None:
        content_type = "application/octet-stream"
    object_id = str(uuid.uuid4())

    # Generate a unique name for the file
    cloud_filename = object_id+file_name

    # Upload the file to the space
    spaces_client.upload_fileobj(
        file,
        space_name,
        cloud_filename,
        ExtraArgs={
            "ACL": "public-read" if is_public else "private",
            "ContentType": content_type
        }
    )

    # Generate a public URL for the file
    url = f"https://{space_name}.{region}.cdn.digitaloceanspaces.com/{space_name}%2F{cloud_filename}"
    return url


def delete_file(spaces_client, space_name, url) -> None:
    """
    Deletes a file from DigitalOcean Spaces.

    :param spaces_client: Your DigitalOcean Spaces client from get_spaces_client()
    :param space_name: Unique name of your space. Can be found at your digitalocean panel
    :param url: URL of the file to be deleted
    :return: None
    :raises Exception: If an error occurs while deleting the file
    """
    try:
        # Extract the filename from the URL
        filename = urllib.parse.unquote(os.path.basename(url)).split('/')[1]

        # Delete the file from DigitalOcean Spaces
        spaces_client.delete_object(Bucket=space_name, Key=filename)
    except Exception as e:
        raise Exception(f"An error occurred while deleting the file: {e}")
