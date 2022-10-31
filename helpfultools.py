import pandas as pd
from colorama import Fore
from datetime import datetime
import actions

# TODO: Move the Sort method from project.py to this file

def print_text(Color, *text):
    print(f"{Color}{text}{Fore.RESET}")

class Searchy:

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def by_id(self, qry):
        qry_result = self.df.loc[qry] if qry in self.df.index else pd.DataFrame(
        )
        return qry_result

    def by_string(self, qry, col):
        qry_df = self.df[col]
        qry_result = self.df.loc[qry_df.str.contains(qry)]
        return qry_result

    def by_num(self, col: str):
        qry_df = self.df[col].replace("-", "0").astype(float)
        min, max = input(f"{Fore.LIGHTMAGENTA_EX}Enter Min: {Fore.RESET}"), input(
            f"{Fore.LIGHTMAGENTA_EX}Enter Max: {Fore.RESET}")
        if min == "":
            min = "0"
        if max == "":
            max = str(qry_df.max())
        try:
            min, max = float(min), float(max)
            qry_result = self.df.loc[(qry_df >= min) & (qry_df <= max)]
        except Exception as e:
            print(f"{Fore.RED}\nPlease enter a valid range!\n{Fore.RESET}")
            qry_result = pd.DataFrame()
        return qry_result

    def by_options(self, qry, col: str, options: list):
        qry_df = self.df[col]
        qry_result = self.df.loc[qry_df == options[qry]]
        return qry_result

    def by_date(self, col, format=r"%Y-%m-%d", time=False):
        print(self.df[col])
        qry_start = input(
            f"{Fore.RED}You can use RegEX\n{Fore.CYAN}Enter range for date \nStart: {Fore.RESET}")
        qry_end = input(f"{Fore.CYAN}End: {Fore.RESET}")
        qry_start, qry_end = pd.to_datetime(actions.date_decoder(
            qry_start, time=time), format=format), pd.to_datetime(actions.date_decoder(qry_end, time=time), format=format)
        if qry_end is not None:
            qry_df = (self.df[col] < qry_end) & (
                self.df[col] > qry_start)
            qry_result = self.df[qry_df]
        else:
            qry_df = self.df[col] > qry_start
            qry_result = self.df[qry_df]
        return qry_result
