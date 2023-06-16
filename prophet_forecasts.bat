call C:\Users\usrocu\Anaconda3\Scripts\activate.bat
call activate forecasting
cd I:\GitHub\fbprophet_forecasts


jupyter nbconvert --execute --to notebook --inplace bssc_sales.ipynb
jupyter nbconvert --execute --to notebook --inplace bssc_support.ipynb
jupyter nbconvert --execute --to notebook --inplace cable_retention.ipynb
jupyter nbconvert --execute --to notebook --inplace cable_sales.ipynb
jupyter nbconvert --execute --to notebook --inplace cable_seniors.ipynb
jupyter nbconvert --execute --to notebook --inplace continuum_bus_sales.ipynb
jupyter nbconvert --execute --to notebook --inplace continuum_resi_sales.ipynb
jupyter nbconvert --execute --to notebook --inplace fs_business.ipynb
jupyter nbconvert --execute --to notebook --inplace fs_residential.ipynb
jupyter nbconvert --execute --to notebook --inplace wireline_retention.ipynb
jupyter nbconvert --execute --to notebook --inplace wireline_sales.ipynb
jupyter nbconvert --execute --to notebook --inplace wireline_seniors.ipynb
jupyter nbconvert --execute --to notebook --inplace wireline_triage.ipynb