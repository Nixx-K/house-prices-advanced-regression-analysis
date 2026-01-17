from os import remove
import matplotlib.pyplot as plt
import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame
import seaborn as sns


def main():
    # ---------- Load Data ----------
    train_path = r"C:\Users\weron\Studia\Semestr 5\Fakultet biblioteki Pythona\Projekt\data\house-prices-advanced-regression-techniques\train.csv"
    test_path = r"C:\Users\weron\Studia\Semestr 5\Fakultet biblioteki Pythona\Projekt\data\house-prices-advanced-regression-techniques\test.csv"

    train = pd.read_csv(train_path)
    test = pd.read_csv(test_path)

    #usuwanie niepotrzebnych kolumn
    train, test = remove_missing(train, test)

    #wypełnianie brakujacych danych za pomocą mediany (z racji odporności mediany na outliery)
    train, test = fill_in_missing(train, test)

    #usuwanie części outlierów
    train = remove_outliers(train)

    #pobieranie wyczyszczonych danych
    train.to_csv(r"C:\Users\weron\PycharmProjects\HousePricesRegression\data\train_postprocessed.csv", index=False)
    test.to_csv(r"C:\Users\weron\PycharmProjects\HousePricesRegression\data\test_postprocessed.csv", index=False)

#usuwanie brakujących danych
def remove_missing(df_train, df_test):
    braki = df_train.isnull().sum().sort_values(ascending=False)

    threshold = len(df_train) / 3
    too_many_missing = braki[braki > threshold]
    names = too_many_missing.index.to_list()

    df_train = df_train.drop(columns=names)
    df_test = df_test.drop(columns=names)
    return df_train, df_test


#uzupełnianie pozostałych brakujących danych
def fill_in_missing(train, test):
    #kolumny numeryczne
    num_cols = train.select_dtypes(include=['int64', 'float64']).columns
    mediany = train[num_cols].median()
    train[num_cols] = train[num_cols].fillna(mediany)
    test_num_cols = [n for n in num_cols if n in test.columns]  # w danych test nie ma kolumny SalePrice
    test[test_num_cols] = test[test_num_cols].fillna(mediany)

    #kolumny kategoryczne
    cat_cols = train.select_dtypes(exclude=['int64', 'float64']).columns
    modes = train[cat_cols].mode().iloc[0]
    train[cat_cols] = train[cat_cols].fillna(modes)
    test[cat_cols] = test[cat_cols].fillna(modes)

    return train, test


#statystyki outlierów z użyciem IQR
def analyze_outliers(df):
    # przy wizualnej analizie outlierów zauważyłam, że wpisuje się w nie wiele wartości z OverallCond, ale uważam ją za ważną kolumnę, więc pomijam przy usuwaniu
    exclude_cols = ['OverallCond', 'OverallQual']
    num_cols = df.select_dtypes(include=['int64', 'float64']).columns.difference(exclude_cols)
    Q1 = df[num_cols].quantile(0.25)
    Q3 = df[num_cols].quantile(0.75)

    IQR = Q3-Q1

    granica_dolna = Q1 - 1.5*IQR
    granica_gorna = Q3 + 1.5*IQR

    outliers = ((df[num_cols] < granica_dolna) | (df[num_cols]>granica_gorna))

    outliers_count = outliers.sum()
    outliers_percentage = outliers_count/len(df)

    return outliers_count, outliers_percentage, outliers, granica_dolna, granica_gorna


#usuwanie outlierów
def remove_outliers(df):
    # analiza outlierów
    outliers_count, outliers_percentage, outliers_mask, dolna, gorna = analyze_outliers(df)

    to_nan = outliers_percentage[outliers_percentage < 0.05].index
    to_clip = outliers_percentage[outliers_percentage >= 0.05].index

    df[to_nan] = df[to_nan].where(~outliers_mask) #ustawianie rzadkich outlierów na NaN
    df[to_clip] = df[to_clip].apply(lambda col: col.clip(lower=dolna[col.name], upper=gorna[col.name]))

    df = df.dropna() #usuwanie wierszy z NaN

    return df


if __name__ == "__main__":
    main()
