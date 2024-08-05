# soda-pandas-dask example
1. Create and activate python 3.9 environment:
```shell
conda create -n soda-pandas-dask-3.9 python=3.9
conda activate soda-pandas-dask-3.9
```
2. Install dependencies (`soda-pandas-dask`):
```shell
pip install -r requirements.txt
```
3. Add your `SODA_CLOUD_API_KEY_ID` and `SODA_CLOUD_API_KEY_SECRET` to your environment (or paste the values into `configuration.yaml`).
4. Run the Soda scan:
```shell
python scan.py
```
Outputs:
```shell
[16:45:35] Deprecated: implicit data_source_name is no longer supported. Make sure to provide a data_source_name when invoking 'add_dask_dataframe()'.
INFO:soda.scan:[16:45:35] By downloading and using Soda Library, you agree to Soda's Terms & Conditions (https://go.soda.io/t&c) and Privacy Policy (https://go.soda.io/privacy). 
INFO:soda.scan:[16:45:39] Scan summary:
INFO:soda.scan:[16:45:39] 1/1 check PASSED: 
INFO:soda.scan:[16:45:39]     cities in dask
INFO:soda.scan:[16:45:39]       row_count > 0 [sodacl_string.yml] [PASSED]
INFO:soda.scan:[16:45:39]         check_value: 47868
INFO:soda.scan:[16:45:39] All is good. No failures. No warnings. No errors.
INFO:soda.scan:[16:45:39] Sending results to Soda Cloud
INFO:soda.scan:[16:45:40] Soda Cloud Trace: 1215404432070063077
```
