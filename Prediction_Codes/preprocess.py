def prep_data(df):

    df = df.assign(hw=df["Height"] * df["Width"])
    df = df.assign(l3_l1_ratio = df["Length3"]/df["Length1"])
    df = df.assign(hw123 = (df["Length1"]+df["Length2"]+df["Length3"])/3*df["hw"])
    df = df.assign(l3l1width = df["Length3"]/df["Length1"]* df["Width"])
    df = df.assign(l3l1height = df["Length3"]/df["Length1"]* df["Height"])

    X = df[["hw","Length1","Length2","Length3","hw123"]].values
    Y = df["Weight"].values
    y=Y.astype(int)

    return X, y