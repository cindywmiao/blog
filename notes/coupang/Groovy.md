Groovy.md

    String SELECT_SQL = """
    a.sku as sku, 
    a.area as area,
    b.skuname as skuname, 
    c.unitname1 as unitname1,
    c.unitname2 as unitname2, 
    c.cate3 as cate3, 
    c.cate4 as cate4, 
    c.cate5 as cate5,
    d.D_7_Sales as D_7_Sales, 
    d.D_6_Sales as D_6_Sales, 
    d.D_5_Sales as D_5_Sales, 
    d.D_4_Sales as D_4_Sales, 
    d.D_3_Sales as D_3_Sales, 
    d.D_2_Sales as D_2_Sales, 
    d.D_1_Sales as D_1_Sales,
    e.D_7_Mean as D_7_Mean, 
    e.D_6_Mean as D_6_Mean, 
    e.D_5_Mean as D_5_Mean, 
    e.D_4_Mean as D_4_Mean, 
    e.D_3_Mean as D_3_Mean, 
    e.D_2_Mean as D_2_Mean, 
    e.D_1_Mean as D_1_Mean,
    a.mean_d1 as mean_d1, 
    a.mean_d2 as mean_d2, 
    a.mean_d3 as mean_d3, 
    a.mean_d4 as mean_d4, 
    a.mean_d5 as mean_d5, 
    a.mean_d6 as mean_d6, 
    a.mean_d7 as mean_d7,
    a.mean_d8 as mean_d8, 
    a.mean_d9 as mean_d9, 
    a.mean_d10 as mean_d10, 
    a.mean_d11 as mean_d11, 
    a.mean_d12 as mean_d12, 
    a.mean_d13 as mean_d13, 
    a.mean_d14 as mean_d14, 
    a.mean_d15 as mean_d15, 
    a.mean_d16 as mean_d16, 
    a.mean_d17 as mean_d17, 
    a.mean_d18 as mean_d18, 
    a.mean_d19 as mean_d19, 
    a.mean_d20 as mean_d20, 
    a.mean_d21 as mean_d21,
    f.mean_d1 as uplift_d1, 
    f.mean_d2 as uplift_d2, 
    f.mean_d3 as uplift_d3, 
    f.mean_d4 as uplift_d4, 
    f.mean_d5 as uplift_d5,
    f.mean_d6 as uplift_d6, 
    f.mean_d7 as uplift_d7, 
    f.mean_d8 as uplift_d8, 
    f.mean_d9 as uplift_d9, 
    f.mean_d10 as uplift_d10,
    f.mean_d11 as uplift_d11, 
    f.mean_d12 as uplift_d12, 
    f.mean_d13 as uplift_d13, 
    f.mean_d14 as uplift_d14, 
    f.mean_d15 as uplift_d15,
    f.mean_d16 as uplift_d16, 
    f.mean_d17 as uplift_d17, 
    f.mean_d18 as uplift_d18, 
    f.mean_d19 as uplift_d19, 
    f.mean_d20 as uplift_d20,
    f.mean_d21 as uplift_d21,
    b.skutype as skutype, 
    b.salestatus as salestatus, 
    b.isalive as isalive,
    f.uplife_flag as uplift_flag
    
"""

    String TABLE_SQL = """
    sku_forecast_result a 
    join sku_status b on a.rundt = b.rundt and a.sku = b.sku 
    join sku_category_hierarchy c on b.rundt = c.rundt and b.mngcateid = c.mngcateid 
    join sku_hist_7sales d on a.rundt = d.rundt and a.sku = d.sku and a.area = d.area 
    join sku_hist_7forecast e on a.rundt = e.rundt and a.sku = e.sku and a.area = e.area 
    join sku_uplift f on a.sku = f.sku and a.rundt = f.rundt 
"""

    String MINI_TABLE_SQL = """
    sku_forecast_result a 
    join sku_status b on a.rundt = b.rundt and a.sku = b.sku 
    join sku_category_hierarchy c on b.rundt = c.rundt and b.mngcateid = c.mngcateid 
    join sku_uplift f on a.sku = f.sku and a.rundt = f.rundt 
"""

    @Many
    @Select("""$SELECT_SQL + from $TABLE_SQL where a.rundt = '${targetDate}' ${query}""")
    List<ForecastResult> findById(@Param("targetDate") String targetDate,
                                  @Param("query") String query)


    @Many
    @Select("""$SELECT_SQL from $TABLE_SQL where a.rundt = '${targetDate}' ${query} limit ${pageSize} offset ${offset}""")
    List<ForecastResult> find(@Param("targetDate") String targetDate,
                                  @Param("query") String query,
                                  @Param("pageSize") int pageSize,
                                  @Param("offset") long offset)


    @One
    @Select("""$SELECT_SQL from $MINI_TABLE_SQL where a.rundt = '${targetDate}' ${query}""")
    int count(@Param("targetDate") String targetDate, @Param("query") String query)