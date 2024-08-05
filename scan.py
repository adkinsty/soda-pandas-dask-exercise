from soda.scan import Scan
import dask.dataframe as dd


def main():

    data = dd.read_csv('./worldcities.csv')
    scan = Scan()
    scan.set_scan_definition_name('test')
    scan.add_dask_dataframe(dataset_name='cities', dask_df=data)
    scan.set_data_source_name('dask')
    check_str = """
    checks for cities:
      - row_count > 0
"""
    scan.add_configuration_yaml_file('./configuration.yaml')
    scan.add_sodacl_yaml_str(check_str)
    scan.set_verbose()
    scan.execute()
    scan.assert_no_checks_fail()


if __name__ == '__main__':
    main()

