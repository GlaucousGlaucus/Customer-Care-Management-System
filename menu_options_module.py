from helpfultools import cls

# All the Menu GUI releated stuff here

menu_main = \
    r"""

                       █     ▄███▄   █▀▄▀█ ████▄    ▄       ███   ▄███▄   ▄███▄   
                       █     █▀   ▀  █ █ █ █   █     █      █  █  █▀   ▀  █▀   ▀  
                       █     ██▄▄    █ ▄ █ █   █ ██   █     █ ▀ ▄ ██▄▄    ██▄▄    
                       ███▄  █▄   ▄▀ █   █ ▀████ █ █  █     █  ▄▀ █▄   ▄▀ █▄   ▄▀ 
                           ▀ ▀███▀      █        █  █ █     ███   ▀███▀   ▀███▀   
                                       ▀         █   ██                           
                                                           
                                                                                          

                                ╔═╗╦ ╦╔═╗╔╦╗╔═╗╔╦╗╔═╗╦═╗  ╔═╗╔═╗╦═╗╔═╗
                                ║  ║ ║╚═╗ ║ ║ ║║║║║╣ ╠╦╝  ║  ╠═╣╠╦╝║╣ 
                                ╚═╝╚═╝╚═╝ ╩ ╚═╝╩ ╩╚═╝╩╚═  ╚═╝╩ ╩╩╚═╚═╝

                                +===================================+
                                       1) Login as Administrator
                                       2) Login as Customer
                                       3) Exit the program
                                +===================================+
"""

# Customer Related
menu_cust = \
    """
                                      ╔═╗╦ ╦╔═╗╔╦╗╔═╗╔╦╗╔═╗╦═╗
                                      ║  ║ ║╚═╗ ║ ║ ║║║║║╣ ╠╦╝
                                      ╚═╝╚═╝╚═╝ ╩ ╚═╝╩ ╩╚═╝╩╚═
                                +===================================+
                                            1) Login
                                            2) Register
                                            3) Back
                                +===================================+
"""
menu_cust_login = \
    """
                                      ╔═╗╦ ╦╔═╗╔╦╗╔═╗╔╦╗╔═╗╦═╗
                                      ║  ║ ║╚═╗ ║ ║ ║║║║║╣ ╠╦╝
                                      ╚═╝╚═╝╚═╝ ╩ ╚═╝╩ ╩╚═╝╩╚═
                                +===================================+
                                            1) Open a ticket
                                            2) View ticket(s)
                                            3) Close a ticket
                                            4) Profile
                                            5) Back
                                +===================================+
"""

# Admin Related
menu_admin = \
    """
                                            ╔═╗╔╦╗╔╦╗╦╔╗╔
                                            ╠═╣ ║║║║║║║║║
                                            ╩ ╩═╩╝╩ ╩╩╝╚╝
                                +===================================+
                                            1) Customers
                                            2) Products
                                            3) Orders
                                            4) Tickets
                                            5) Back
                                +===================================+
"""

maC = \
    """
                               ╔═╗╔╦╗╔╦╗╦╔╗╔ | ╔═╗╦ ╦╔═╗╔╦╗╔═╗╔╦╗╔═╗╦═╗
                               ╠═╣ ║║║║║║║║║ | ║  ║ ║╚═╗ ║ ║ ║║║║║╣ ╠╦╝
                               ╩ ╩═╩╝╩ ╩╩╝╚╝ | ╚═╝╚═╝╚═╝ ╩ ╚═╝╩ ╩╚═╝╩╚═
                                +===================================+
                                        1) Show all Customers
                                        2) Search
                                        3) Add a customer
                                        4) Modify a customer
                                        5) Delete a customer
                                        6) Sort
                                        7) Data Analysis
                                        8) Back
                                +===================================+
"""
maC_Search = \
    """
                    ╔═╗╔╦╗╔╦╗╦╔╗╔ | ╔═╗╦ ╦╔═╗╔╦╗╔═╗╔╦╗╔═╗╦═╗ | ╔═╗╔═╗╔═╗╦═╗╔═╗╦ ╦
                    ╠═╣ ║║║║║║║║║ | ║  ║ ║╚═╗ ║ ║ ║║║║║╣ ╠╦╝ | ╚═╗║╣ ╠═╣╠╦╝║  ╠═╣
                    ╩ ╩═╩╝╩ ╩╩╝╚╝ | ╚═╝╚═╝╚═╝ ╩ ╚═╝╩ ╩╚═╝╩╚═ | ╚═╝╚═╝╩ ╩╩╚═╚═╝╩ ╩
                                +===================================+
                                        1) Search by ID
                                        2) Search by First Name
                                        3) Search by Last Name
                                        4) Search by DOB
                                        5) Search by Gender
                                        6) Search by Address
                                        7) Search by Country
                                        8) Search by City
                                        9) Search by State
                                        10) Search by Pincode
                                        11) Search by Phone
                                        12) Search by email
                                        13) Seach by Prime
                                        14) Reset Dataframe
                                        15) Back
                                +===================================+
"""
maC_Sort =  \
    """
                      ╔═╗╔╦╗╔╦╗╦╔╗╔ | ╔═╗╦ ╦╔═╗╔╦╗╔═╗╔╦╗╔═╗╦═╗ | ╔═╗╔═╗╦═╗╔╦╗
                      ╠═╣ ║║║║║║║║║ | ║  ║ ║╚═╗ ║ ║ ║║║║║╣ ╠╦╝ | ╚═╗║ ║╠╦╝ ║ 
                      ╩ ╩═╩╝╩ ╩╩╝╚╝ | ╚═╝╚═╝╚═╝ ╩ ╚═╝╩ ╩╚═╝╩╚═ | ╚═╝╚═╝╩╚═ ╩ 
                                +===================================+
                                        1) Sort by ID
                                        2) Sort by First Name
                                        3) Sort by Last Name
                                        4) Sort by DOB
                                        5) Sort by Gender
                                        6) Sort by Address
                                        7) Sort by Country
                                        8) Sort by City
                                        9) Sort by State
                                        10) Sort by Pincode
                                        11) Sort by Phone
                                        12) Sort by email
                                        13) Sort by Prime
                                        14) Back
                                +===================================+
"""
maC_DataAnalysis =  \
    """
              ╔═╗╔╦╗╔╦╗╦╔╗╔ | ╔═╗╦ ╦╔═╗╔╦╗╔═╗╔╦╗╔═╗╦═╗ | ╔╦╗╔═╗╔╦╗╔═╗  ╔═╗╔╗╔╔═╗╦ ╦ ╦╔═╗╦╔═╗
              ╠═╣ ║║║║║║║║║ | ║  ║ ║╚═╗ ║ ║ ║║║║║╣ ╠╦╝ |  ║║╠═╣ ║ ╠═╣  ╠═╣║║║╠═╣║ ╚╦╝╚═╗║╚═╗
              ╩ ╩═╩╝╩ ╩╩╝╚╝ | ╚═╝╚═╝╚═╝ ╩ ╚═╝╩ ╩╚═╝╩╚═ | ═╩╝╩ ╩ ╩ ╩ ╩  ╩ ╩╝╚╝╩ ╩╩═╝╩ ╚═╝╩╚═╝
                                +===================================+
                                            1) Pie Chart
                                            2) Bar Graph
                                            3) Back
                                +===================================+
"""
maC_da_PieChart =  \
    """
              ╔═╗╔╦╗╔╦╗╦╔╗╔ | ╔═╗╦ ╦╔═╗╔╦╗╔═╗╔╦╗╔═╗╦═╗ | ╔╦╗╔═╗╔╦╗╔═╗  ╔═╗╔╗╔╔═╗╦ ╦ ╦╔═╗╦╔═╗
              ╠═╣ ║║║║║║║║║ | ║  ║ ║╚═╗ ║ ║ ║║║║║╣ ╠╦╝ |  ║║╠═╣ ║ ╠═╣  ╠═╣║║║╠═╣║ ╚╦╝╚═╗║╚═╗
              ╩ ╩═╩╝╩ ╩╩╝╚╝ | ╚═╝╚═╝╚═╝ ╩ ╚═╝╩ ╩╚═╝╩╚═ | ═╩╝╩ ╩ ╩ ╩ ╩  ╩ ╩╝╚╝╩ ╩╩═╝╩ ╚═╝╩╚═╝
                                +===================================+
                                            1) Gender
                                            2) Country
                                            3) State
                                            4) Prime
                                            5) Back
                                +===================================+
"""
maC_da_BarGraph =  \
    """
              ╔═╗╔╦╗╔╦╗╦╔╗╔ | ╔═╗╦ ╦╔═╗╔╦╗╔═╗╔╦╗╔═╗╦═╗ | ╔╦╗╔═╗╔╦╗╔═╗  ╔═╗╔╗╔╔═╗╦ ╦ ╦╔═╗╦╔═╗
              ╠═╣ ║║║║║║║║║ | ║  ║ ║╚═╗ ║ ║ ║║║║║╣ ╠╦╝ |  ║║╠═╣ ║ ╠═╣  ╠═╣║║║╠═╣║ ╚╦╝╚═╗║╚═╗
              ╩ ╩═╩╝╩ ╩╩╝╚╝ | ╚═╝╚═╝╚═╝ ╩ ╚═╝╩ ╩╚═╝╩╚═ | ═╩╝╩ ╩ ╩ ╩ ╩  ╩ ╩╝╚╝╩ ╩╩═╝╩ ╚═╝╩╚═╝
                                +===================================+
                                        1) Age of Customers
                                        2) Back
                                +===================================+
"""

maP =  \
    """
                               ╔═╗╔╦╗╔╦╗╦╔╗╔ | ╔═╗╦═╗╔═╗╔╦╗╦ ╦╔═╗╔╦╗╔═╗
                               ╠═╣ ║║║║║║║║║ | ╠═╝╠╦╝║ ║ ║║║ ║║   ║ ╚═╗
                               ╩ ╩═╩╝╩ ╩╩╝╚╝ | ╩  ╩╚═╚═╝═╩╝╚═╝╚═╝ ╩ ╚═╝
                                +===================================+
                                        1) Show all Products
                                        2) Search
                                        3) Add a product
                                        4) Modify a product
                                        5) Delete a product
                                        6) Sort
                                        7) Data Analysis
                                        8) Back
                                +===================================+
"""
maP_Search =  \
    """
                      ╔═╗╔╦╗╔╦╗╦╔╗╔ | ╔═╗╦═╗╔═╗╔╦╗╦ ╦╔═╗╔╦╗╔═╗ | ╔═╗╔═╗╔═╗╦═╗╔═╗╦ ╦
                      ╠═╣ ║║║║║║║║║ | ╠═╝╠╦╝║ ║ ║║║ ║║   ║ ╚═╗ | ╚═╗║╣ ╠═╣╠╦╝║  ╠═╣
                      ╩ ╩═╩╝╩ ╩╩╝╚╝ | ╩  ╩╚═╚═╝═╩╝╚═╝╚═╝ ╩ ╚═╝ | ╚═╝╚═╝╩ ╩╩╚═╚═╝╩ ╩
                                +===================================+
                                        1) Search by ID
                                        2) Search by Name
                                        3) Search by Manufacturer
                                        4) Search by Category
                                        5) Search by In-Stock
                                        6) Search by Average Rating
                                        7) Search by Returnable
                                        8) Search by Days to Return
                                        9) Back
                                        10) Reset Dataframe
                                +===================================+
"""
maP_Search_SearchByReturnable =  \
    """
                      ╔═╗╔╦╗╔╦╗╦╔╗╔ | ╔═╗╦═╗╔═╗╔╦╗╦ ╦╔═╗╔╦╗╔═╗ | ╔═╗╔═╗╔═╗╦═╗╔═╗╦ ╦
                      ╠═╣ ║║║║║║║║║ | ╠═╝╠╦╝║ ║ ║║║ ║║   ║ ╚═╗ | ╚═╗║╣ ╠═╣╠╦╝║  ╠═╣
                      ╩ ╩═╩╝╩ ╩╩╝╚╝ | ╩  ╩╚═╚═╝═╩╝╚═╝╚═╝ ╩ ╚═╝ | ╚═╝╚═╝╩ ╩╩╚═╚═╝╩ ╩
                                +===================================+
                                           1) Returnable
                                           2) Exchange Only
                                           3) Non Returnable
                                           4) Back
                                +===================================+
"""
maP_Sort =  \
    """
                         ╔═╗╔╦╗╔╦╗╦╔╗╔ | ╔═╗╦═╗╔═╗╔╦╗╦ ╦╔═╗╔╦╗╔═╗ | ╔═╗╔═╗╦═╗╔╦╗
                         ╠═╣ ║║║║║║║║║ | ╠═╝╠╦╝║ ║ ║║║ ║║   ║ ╚═╗ | ╚═╗║ ║╠╦╝ ║ 
                         ╩ ╩═╩╝╩ ╩╩╝╚╝ | ╩  ╩╚═╚═╝═╩╝╚═╝╚═╝ ╩ ╚═╝ | ╚═╝╚═╝╩╚═ ╩ 
                                +===================================+
                                        1) Sort by ID
                                        2) Sort by Name
                                        3) Sort by Manufacturer
                                        4) Sort by Category
                                        5) Sort by In-Stock
                                        6) Sort by Average Rating
                                        7) Sort by Returnable
                                        8) Sort by Days to Return
                                        9) Back
                                +===================================+
"""
maP_DataAnalysis =  \
    """
                ╔═╗╔╦╗╔╦╗╦╔╗╔ | ╔═╗╦═╗╔═╗╔╦╗╦ ╦╔═╗╔╦╗╔═╗ | ╔╦╗╔═╗╔╦╗╔═╗  ╔═╗╔╗╔╔═╗╦ ╦ ╦╔═╗╦╔═╗
                ╠═╣ ║║║║║║║║║ | ╠═╝╠╦╝║ ║ ║║║ ║║   ║ ╚═╗ |  ║║╠═╣ ║ ╠═╣  ╠═╣║║║╠═╣║ ╚╦╝╚═╗║╚═╗
                ╩ ╩═╩╝╩ ╩╩╝╚╝ | ╩  ╩╚═╚═╝═╩╝╚═╝╚═╝ ╩ ╚═╝ | ═╩╝╩ ╩ ╩ ╩ ╩  ╩ ╩╝╚╝╩ ╩╩═╝╩ ╚═╝╩╚═╝
                                +===================================+
                                        1) Categories (In-Stock)
                                        2) Returnable
                                        3) Average Rating
                                        99) Back
                                +===================================+
"""
maP_da_PieChart =  \
    """
3) Back
"""

maO =  \
    """
                                  ╔═╗╔╦╗╔╦╗╦╔╗╔ | ╔═╗╦═╗╔╦╗╔═╗╦═╗╔═╗
                                  ╠═╣ ║║║║║║║║║ | ║ ║╠╦╝ ║║║╣ ╠╦╝╚═╗
                                  ╩ ╩═╩╝╩ ╩╩╝╚╝ | ╚═╝╩╚══╩╝╚═╝╩╚═╚═╝
                                +===================================+
                                           1) Show all orders
                                           2) Search
                                           3) Add an order
                                           4) Modify an order
                                           5) Delete an order
                                           6) Sort
                                           7) Back
                                +===================================+
"""
maO_Search =  \
    """
                         ╔═╗╔╦╗╔╦╗╦╔╗╔ | ╔═╗╦═╗╔╦╗╔═╗╦═╗╔═╗ | ╔═╗╔═╗╔═╗╦═╗╔═╗╦ ╦
                         ╠═╣ ║║║║║║║║║ | ║ ║╠╦╝ ║║║╣ ╠╦╝╚═╗ | ╚═╗║╣ ╠═╣╠╦╝║  ╠═╣
                         ╩ ╩═╩╝╩ ╩╩╝╚╝ | ╚═╝╩╚══╩╝╚═╝╩╚═╚═╝ | ╚═╝╚═╝╩ ╩╩╚═╚═╝╩ ╩
                                +===================================+
                                     1) Search By Order ID
                                     2) Search by Customer ID
                                     3) Search by Customer FirstName
                                     4) Search by Customer LastName
                                     5) Search by Product ID
                                     6) Search by Product Name
                                     7) Search by Quantity
                                     8) Search by Total Price
                                     9) Search by Date of Order
                                     10) Search by Status
                                     11) Search by Address
                                     12) Back
                                     13) Reset Dataframe
                                +===================================+
"""
maO_Sort =  \
    """
                         ╔═╗╔╦╗╔╦╗╦╔╗╔ | ╔═╗╦═╗╔╦╗╔═╗╦═╗╔═╗ | ╔═╗╔═╗╦═╗╔╦╗
                         ╠═╣ ║║║║║║║║║ | ║ ║╠╦╝ ║║║╣ ╠╦╝╚═╗ | ╚═╗║ ║╠╦╝ ║ 
                         ╩ ╩═╩╝╩ ╩╩╝╚╝ | ╚═╝╩╚══╩╝╚═╝╩╚═╚═╝ | ╚═╝╚═╝╩╚═ ╩ 
                                +===================================+
                                       1) Sort By Order ID
                                       2) Sort by Customer ID
                                       3) Sort by Customer FirstName
                                       4) Sort by Customer LastName
                                       5) Sort by Product ID
                                       6) Sort by Product Name
                                       7) Sort by Quantity
                                       8) Sort by Total Price
                                       9) Sort by Date of Order
                                       10) Sort by Status
                                       11) Sort by Address 
                                       12) Back
                                +===================================+
"""

maT =  \
    """
                                 ╔═╗╔╦╗╔╦╗╦╔╗╔ | ╔╦╗╦╔═╗╦╔═╔═╗╔╦╗╔═╗
                                 ╠═╣ ║║║║║║║║║ |  ║ ║║  ╠╩╗║╣  ║ ╚═╗
                                 ╩ ╩═╩╝╩ ╩╩╝╚╝ |  ╩ ╩╚═╝╩ ╩╚═╝ ╩ ╚═╝
                                +===================================+
                                        1) Show all Tickets
                                        2) Search
                                        3) Add a ticket
                                        4) Modify a ticket
                                        5) Delete a ticket
                                        6) Sort
                                        7) Data Analysis
                                        8) Report Generation
                                        9) Message Generation
                                        10) Back
                                +===================================+
"""
maT_Search =  \
    """
                        ╔═╗╔╦╗╔╦╗╦╔╗╔ | ╔╦╗╦╔═╗╦╔═╔═╗╔╦╗╔═╗  | ╔═╗╔═╗╔═╗╦═╗╔═╗╦ ╦
                        ╠═╣ ║║║║║║║║║ |  ║ ║║  ╠╩╗║╣  ║ ╚═╗  | ╚═╗║╣ ╠═╣╠╦╝║  ╠═╣
                        ╩ ╩═╩╝╩ ╩╩╝╚╝ |  ╩ ╩╚═╝╩ ╩╚═╝ ╩ ╚═╝  | ╚═╝╚═╝╩ ╩╩╚═╚═╝╩ ╩
                                +===================================+
                                      1) Search by Ticket ID
                                      2) Search by Customer ID
                                      3) Search by Order ID
                                      4) Search by Product Name
                                      5) Search by Product Category
                                      6) Search by Customer's FirstName
                                      7) Search by Customer's Phone
                                      8) Search by Status
                                      9) Search by IssueCategory
                                      10) Search by Issue
                                      11) Search by Date Opened
                                      12) Search by Data Closed
                                      13) Search by HoursTaken
                                      14) Search by FirstResponseTime
                                      15) Search by Replies
                                      16) Search by Customer Satisfaction
                                      17) Back
                                +===================================+
"""
maT_Sort =  \
    """
                            ╔═╗╔╦╗╔╦╗╦╔╗╔ | ╔╦╗╦╔═╗╦╔═╔═╗╔╦╗╔═╗ | ╔═╗╔═╗╦═╗╔╦╗
                            ╠═╣ ║║║║║║║║║ |  ║ ║║  ╠╩╗║╣  ║ ╚═╗ | ╚═╗║ ║╠╦╝ ║ 
                            ╩ ╩═╩╝╩ ╩╩╝╚╝ |  ╩ ╩╚═╝╩ ╩╚═╝ ╩ ╚═╝ | ╚═╝╚═╝╩╚═ ╩ 
                                +===================================+
                                       1) Sort by Ticket ID
                                       2) Sort by Customer ID
                                       3) Sort by Order ID
                                       4) Sort by Product Name
                                       5) Sort by Product Category
                                       6) Sort by Customer's FirstName
                                       7) Sort by Customer's Phone
                                       8) Sort by Status
                                       9) Sort by IssueCategory
                                       10) Sort by Issue
                                       11) Sort by Date Opened
                                       12) Sort by Data Closed
                                       13) Sort by HoursTaken
                                       14) Sort by FirstResponseTime
                                       15) Sort by Replies
                                       16) Sort by Customer Satisfaction
                                       17) Back
                                +===================================+
"""
maT_DataAnalysis =  \
    """
               ╔═╗╔╦╗╔╦╗╦╔╗╔ | ╔╦╗╦╔═╗╦╔═╔═╗╔╦╗╔═╗ | ╔╦╗╔═╗╔╦╗╔═╗  ╔═╗╔╗╔╔═╗╦ ╦ ╦╔═╗╦╔═╗
               ╠═╣ ║║║║║║║║║ |  ║ ║║  ╠╩╗║╣  ║ ╚═╗ |  ║║╠═╣ ║ ╠═╣  ╠═╣║║║╠═╣║ ╚╦╝╚═╗║╚═╗
               ╩ ╩═╩╝╩ ╩╩╝╚╝ |  ╩ ╩╚═╝╩ ╩╚═╝ ╩ ╚═╝ | ═╩╝╩ ╩ ╩ ╩ ╩  ╩ ╩╝╚╝╩ ╩╩═╝╩ ╚═╝╩╚═╝
                                +===================================+
                                            1) Pie Chart
                                            2) Bar Graph
                                            3) Other Graph
                                            4) Back
                                +===================================+
"""
maT_DA_PieChart =  \
    """
               ╔═╗╔╦╗╔╦╗╦╔╗╔ | ╔╦╗╦╔═╗╦╔═╔═╗╔╦╗╔═╗ | ╔╦╗╔═╗╔╦╗╔═╗  ╔═╗╔╗╔╔═╗╦ ╦ ╦╔═╗╦╔═╗
               ╠═╣ ║║║║║║║║║ |  ║ ║║  ╠╩╗║╣  ║ ╚═╗ |  ║║╠═╣ ║ ╠═╣  ╠═╣║║║╠═╣║ ╚╦╝╚═╗║╚═╗
               ╩ ╩═╩╝╩ ╩╩╝╚╝ |  ╩ ╩╚═╝╩ ╩╚═╝ ╩ ╚═╝ | ═╩╝╩ ╩ ╩ ╩ ╩  ╩ ╩╝╚╝╩ ╩╩═╝╩ ╚═╝╩╚═╝
                                +===================================+
                                            1) Status
                                            2) Product Category
                                            3) Back
                                +===================================+
"""
maT_DA_BarGraph =  \
    """
               ╔═╗╔╦╗╔╦╗╦╔╗╔ | ╔╦╗╦╔═╗╦╔═╔═╗╔╦╗╔═╗ | ╔╦╗╔═╗╔╦╗╔═╗  ╔═╗╔╗╔╔═╗╦ ╦ ╦╔═╗╦╔═╗
               ╠═╣ ║║║║║║║║║ |  ║ ║║  ╠╩╗║╣  ║ ╚═╗ |  ║║╠═╣ ║ ╠═╣  ╠═╣║║║╠═╣║ ╚╦╝╚═╗║╚═╗
               ╩ ╩═╩╝╩ ╩╩╝╚╝ |  ╩ ╩╚═╝╩ ╩╚═╝ ╩ ╚═╝ | ═╩╝╩ ╩ ╩ ╩ ╩  ╩ ╩╝╚╝╩ ╩╩═╝╩ ╚═╝╩╚═╝
                                +===================================+
                                1) Tickets Opened in a year (each Month)
                                2) Tickets Closed in a year (each Month)
                                3) Both 1 And 2
                                4) Back
                                +===================================+
"""
maT_DA_OtherGraph =  \
    """
               ╔═╗╔╦╗╔╦╗╦╔╗╔ | ╔╦╗╦╔═╗╦╔═╔═╗╔╦╗╔═╗ | ╔╦╗╔═╗╔╦╗╔═╗  ╔═╗╔╗╔╔═╗╦ ╦ ╦╔═╗╦╔═╗
               ╠═╣ ║║║║║║║║║ |  ║ ║║  ╠╩╗║╣  ║ ╚═╗ |  ║║╠═╣ ║ ╠═╣  ╠═╣║║║╠═╣║ ╚╦╝╚═╗║╚═╗
               ╩ ╩═╩╝╩ ╩╩╝╚╝ |  ╩ ╩╚═╝╩ ╩╚═╝ ╩ ╚═╝ | ═╩╝╩ ╩ ╩ ╩ ╩  ╩ ╩╝╚╝╩ ╩╩═╝╩ ╚═╝╩╚═╝
                                +===================================+
                                    1) Avg. Time Taken each month
                                    2) Avg. Response Time
                                    3) Avg. replies
                                    4) Customer Satisfaction 
                                    5) Back
                                +===================================+
"""
maT_ReportGeneration =  \
    """
                        ╔═╗╔╦╗╔╦╗╦╔╗╔ | ╔╦╗╦╔═╗╦╔═╔═╗╔╦╗╔═╗ | ╦═╗╔═╗╔═╗╔═╗╦═╗╔╦╗
                        ╠═╣ ║║║║║║║║║ |  ║ ║║  ╠╩╗║╣  ║ ╚═╗ | ╠╦╝║╣ ╠═╝║ ║╠╦╝ ║ 
                        ╩ ╩═╩╝╩ ╩╩╝╚╝ |  ╩ ╩╚═╝╩ ╩╚═╝ ╩ ╚═╝ | ╩╚═╚═╝╩  ╚═╝╩╚═ ╩ 
                                +===================================+
                                            1) Summarise
                                            2) Back
                                +===================================+
"""
maT_RG_Summarize =  \
    """
                        ╔═╗╔╦╗╔╦╗╦╔╗╔ | ╔╦╗╦╔═╗╦╔═╔═╗╔╦╗╔═╗ | ╦═╗╔═╗╔═╗╔═╗╦═╗╔╦╗
                        ╠═╣ ║║║║║║║║║ |  ║ ║║  ╠╩╗║╣  ║ ╚═╗ | ╠╦╝║╣ ╠═╝║ ║╠╦╝ ║ 
                        ╩ ╩═╩╝╩ ╩╩╝╚╝ |  ╩ ╩╚═╝╩ ╩╚═╝ ╩ ╚═╝ | ╩╚═╚═╝╩  ╚═╝╩╚═ ╩ 
                                +===================================+
                                            1) Today
                                            2) This week
                                            3) This month
                                            4) This year
                                            5) Custom
                                            6) Back
                                +===================================+
"""
maT_MessageGeneration =  \
    """
                        ╔═╗╔╦╗╔╦╗╦╔╗╔ | ╔╦╗╦╔═╗╦╔═╔═╗╔╦╗╔═╗ | ╔╦╗╔═╗╔═╗╔═╗╔═╗╔═╗╔═╗
                        ╠═╣ ║║║║║║║║║ |  ║ ║║  ╠╩╗║╣  ║ ╚═╗ | ║║║║╣ ╚═╗╚═╗╠═╣║ ╦║╣ 
                        ╩ ╩═╩╝╩ ╩╩╝╚╝ |  ╩ ╩╚═╝╩ ╩╚═╝ ╩ ╚═╝ | ╩ ╩╚═╝╚═╝╚═╝╩ ╩╚═╝╚═╝
                                +===================================+
                                       1) Generate from Template
                                       2) Custom
                                       3) Back
                                +===================================+
"""
maT_MG_Generatefromtemplate =  \
    """
                        ╔═╗╔╦╗╔╦╗╦╔╗╔ | ╔╦╗╦╔═╗╦╔═╔═╗╔╦╗╔═╗ | ╔╦╗╔═╗╔═╗╔═╗╔═╗╔═╗╔═╗
                        ╠═╣ ║║║║║║║║║ |  ║ ║║  ╠╩╗║╣  ║ ╚═╗ | ║║║║╣ ╚═╗╚═╗╠═╣║ ╦║╣ 
                        ╩ ╩═╩╝╩ ╩╩╝╚╝ |  ╩ ╩╚═╝╩ ╩╚═╝ ╩ ╚═╝ | ╩ ╩╚═╝╚═╝╚═╝╩ ╩╚═╝╚═╝
                                +===================================+
                                       1) First Response
                                       2) Request Denied
                                       3) Request acknowledged
                                       4) Back
                                +===================================+
"""
maT_MG_Custom =  \
    """
                        ╔═╗╔╦╗╔╦╗╦╔╗╔ | ╔╦╗╦╔═╗╦╔═╔═╗╔╦╗╔═╗ | ╔╦╗╔═╗╔═╗╔═╗╔═╗╔═╗╔═╗
                        ╠═╣ ║║║║║║║║║ |  ║ ║║  ╠╩╗║╣  ║ ╚═╗ | ║║║║╣ ╚═╗╚═╗╠═╣║ ╦║╣ 
                        ╩ ╩═╩╝╩ ╩╩╝╚╝ |  ╩ ╩╚═╝╩ ╩╚═╝ ╩ ╚═╝ | ╩ ╩╚═╝╚═╝╚═╝╩ ╩╚═╝╚═╝
                                +===================================+
                                            1) Quanta
                                            2) Back
                                +===================================+
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

def print_menu(menu_level):
    cls()
    print(menu_options[menu_level])
