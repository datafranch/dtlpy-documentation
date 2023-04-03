def section1():
    # param name: the driver name
    # param driver_type: ExternalStorage.AZUREBLOB
    # param integration_id: the integration id
    # param bucket_name: the external bucket name
    # param project_id:
    # param allow_external_delete:
    # param path: Optional. By default, path is the root folder. Path is case sensitive.
    # return: driver object
    import dtlpy as dl
    project = dl.projects.get('prject_name')
    driver = project.drivers.create(name='driver_name',
                                    driver_type=dl.ExternalStorage.AZUREBLOB,
                                    integration_id='integration_id',
                                    bucket_name='bucket_name',
                                    allow_external_delete=True,
                                    path="")


def section2():
    # create a dataset from a driver name, you can also create by the driver ID
    import dtlpy as dl
    project: dl.Project
    dataset = project.datasets.create(dataset_name=dataset_name,
                                      driver=driver)
    dataset.sync()
