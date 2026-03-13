def calculate_stats(df):

    # Weekly
    if "Weekly Target" in df.columns and "Weekly Done" in df.columns:
        df["Weekly Need"] = df["Weekly Target"] - df["Weekly Done"]
        df["Weekly Progress"] = (
            df["Weekly Done"] / df["Weekly Target"]
        ).fillna(0)

    # Monitor
    if "Monitor Target" in df.columns and "On Monitor" in df.columns:
        df["Monitor Need"] = df["Monitor Target"] - df["On Monitor"]

    # Commission
    if "Com Target" in df.columns and "Com On" in df.columns:
        df["Com Short"] = df["Com Target"] - df["Com On"]

    return df