import dlt

@dlt.table
def demo():
    return spark.range(10)