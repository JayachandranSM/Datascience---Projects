class univariate():

    def QuanQual(dataset):
        Quan = []
        Qual = []

        for ColumnName in dataset.columns:
            #print(ColumnName)
            if (dataset[ColumnName].dtypes == 'O'):
                Qual.append(ColumnName)
            else:
                Quan.append(ColumnName)
        return Quan,Qual