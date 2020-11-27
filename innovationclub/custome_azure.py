from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'innovationstatic' # Must be replaced by your <storage_account_name>
    account_key = 'nedPdSfF/TZGPfbhSYqMJ005SBCLHQ71DbXUV3R3WWx0fu1VgqeH0+JGtQ89TP9W0eJeidFUKxCbi6xj6X+m3A==' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'innovationstatic' # Must be replaced by your storage_account_name
    account_key = 'Xl9lCEzjsMakpFs9YyVEDzlFXO2nCsaDZzRgYCjmKPzv+r2qzPWk9XTaP4UJdhhnIQGDO54r3JHxWrwm99hG7A==' # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None
