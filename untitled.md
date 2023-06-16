appended_data = []
for name in service:
    query = f'''SELECT "A1"."DateTime",
                "A1"."Queue",
                "A1"."Actual_AHT",
                "A1"."Actual_CV",
                "A1"."Forecasted_AHT",
                "A1"."Forecasted_CV"
        FROM "CCO_WFM"."Queue_Analytics" "A1"
        WHERE "A1"."Queue" = '{name}'
            AND "A1"."DateTime" < TO_DATE('{first_day}','YYYY-MM-DD')'''
    
    new_query = f'''SELECT 
                        [DateTime],
                        [Queue],
                        [Actual_AHT],
                        [Actual_CV],
                        [Actual_FTE],
                        [Forecasted_AHT],
                        [Forecasted_CV]
                        
                    FROM [BPMAINDB].[dbo].[V_AdHoc_PerformanceStatistics]
                    WHERE ([Queue] = '{name}') AND ([DateTime] < '{first_day}')
                    AND ([UserName] = 'satverintwrkoptmgmt')'''
    data = pd.read_sql(new_query, verint)
    appended_data.append(data)
appended_data = pd.concat(appended_data)
appended_data.tail(3)