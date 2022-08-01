menu_main = \
"""
1) Login as Administrator
2) Login as Customer
3) Exit the program
"""

# Customer Related
menu_cust = \
"""
1) Login
2) Register
3) Back
"""
menu_cust_login = \
"""
1) Open a ticket
2) View ticket(s)
3) Close a ticket
4) Back
"""

# Admin Related
menu_admin = \
"""
1) Customers
2) Products
3) Orders
4) Tickets
5) Back
"""

maC = \
"""
1) Show all Customers
2) Search
3) Add a customer
4) Modify a customer
5) Delete a customer
6) Sort
7) Data Analysis
8) Back
"""
maC_Search = \
"""
1) Search by ID
2) Search by Name
3) Search by DOB
4) Search by Gender
5) Search by Address
6) Search by Country
7) Search by City
8) Search by State
9) Search by Pincode
10) Search by Phone
11) Search by email
12) Seach by Prime
13) Back
"""
maC_Sort =  \
"""
1) Sort by ID
2) Sort by Name
3) Sort by DOB
4) Sort by Gender
5) Sort by Address
6) Sort by Country
7) Sort by City
8) Sort by State
9) Sort by Pincode
10) Sort by Phone
11) Sort by email
12) Sort by Prime
13) Back
"""
maC_DataAnalysis =  \
"""
"""
maC_da_PieChart =  \
"""
"""
maC_da_BarGraph =  \
"""
"""

maP =  \
"""
"""
maP_Search =  \
"""
"""
maP_Search_SearchByReturnable =  \
"""
"""
maP_Sort =  \
"""
"""
maP_DataAnalysis =  \
"""
"""
maP_da_PieChart =  \
"""
"""

maO =  \
"""
"""
maO_Search =  \
"""
"""
maO_Sort =  \
"""
"""

maT =  \
"""
"""
maT_Search =  \
"""
"""
maT_Sort =  \
"""
"""
maT_DataAnalysis =  \
"""
"""
maT_DA_PieChart =  \
"""
"""
maT_DA_BarGraph =  \
"""
"""
maT_DA_OtherGraph =  \
"""
"""
maT_ReportGeneration =  \
"""
"""
maT_RG_Summarize =  \
"""
"""
maT_MessageGeneration =  \
"""
"""
maT_MG_Generatefromtemplate =  \
"""
"""
maT_MG_Custom =  \
"""
"""

menu_options = {
    "0": menu_main,
    "1": menu_admin,
        "1.1": maC,
            "1.1.1": maC_Search,
            "1.1.2": maC_Sort,
            "1.1.3": maC_DataAnalysis,
                "1.1.3.1": maC_da_PieChart,
                "1.1.3.2": maC_da_BarGraph,
        "1.2": maP,
            "1.2.1": maP_Search,
                "1.2.1.1": maP_Search_SearchByReturnable,
            "1.2.2": maP_Sort,
            "1.2.3": maP_DataAnalysis,
                "1.2.3.1": maP_da_PieChart,
        "1.3": maO,
            "1.3.1": maO_Search,
            "1.3.2": maO_Sort,
        "1.4": maT,
            "1.4.1": maT_Search,
            "1.4.2": maT_Sort,
            "1.4.3": maT_DataAnalysis,
                "1.4.3.1": maT_DA_PieChart,
                "1.4.3.2": maT_DA_BarGraph,
                "1.4.3.3": maT_DA_OtherGraph,
            "1.4.4": maT_ReportGeneration,
                "1.4.4.1": maT_RG_Summarize,
            "1.4.5": maT_MessageGeneration,
                "1.4.5.1": maT_MG_Generatefromtemplate,
                "1.4.5.2": maT_MG_Custom,
    "2": menu_cust,
        "2.1": menu_cust_login
}