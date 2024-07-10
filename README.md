![White Minimalist Profile LinkedIn Banner](https://github.com/jaggaraj/STYLELABS/assets/123171411/f4a777d9-8180-45af-b01c-126da67f3c44)

IMPLEMENING CERTAIN DATA STORAGE AND DATA ANALYSIS TECHNOLOGIES AT STYLE LABS PVT LTD.

#  INTRODUCTION
Style labs is primarily focused on providing clients with high-quality designer clothing. They put a lot of effort into creating unique, superior designs that satisfy a range of stylistic preferences. As its business grows, the company is thinking about making decisions based on data, and it has begun implementing certain data storage and data analysis technologies.

#  PROBLEMS

MARKET SEGMENTATION

DATA STORAGE

SALES TRACKING

DESIGNING COMBOS

SENTIMENT ANALYSIS

PREDICTING FUTURE TRENDS


#  TOOLS

 ![R](https://github.com/jaggarajununna/STYLELABS/assets/123171411/19c06d87-d0ea-472b-9528-84a28580775a)
 
# SEGMENTATION OF MARKET

The 100 responses were divided into two groups with sizes of 47 and 53, respectively, via the k-modes clustering method. The combination of age group, salary, event, and preferences determined the clustering. The modes, or most frequent values, for each cluster were revealed. These revealed that Cluster 1 was defined by individuals between the ages of 36 and 45 who made over $100,000 per year, attended festivals, and preferred trendy styles, while Cluster 2 was defined by individuals between the ages of 26 and 35 who made over $50,000 per year, went on dates, and preferred casual styles.Responses are divided into two segments; based on this, we can design marketing strategies accordingly to cater to the preferences of each segement of customers.

[CLICK HERE TO VIEW](https://github.com/jaggaraj/STYLELABS/blob/main/CLUSTER%20ANALYSIS.pdf) R

[CLICK HERE TO VIEW](https://github.com/jaggaraj/STYLELABS/blob/main/cluster%20analysis.pdf) SPSS
 

# MY SQL DATA BASE FOR HUMAN RESOURCES MANAGEMENT OPERATION
   
This document presents the schema for a mysql database named "stylelabs_hr" designed to store and manage employee-related information. The schema consists of seven interconnected tables: cost_center, education_details, employee_details, emp_designation_promotion, recruitment_type, salary_band, and training_details.
The cost_center table stores details about the employee's cost center, including the employee code, strategic business unit (sbu) address, and joining date. The education_details table records the highest educational qualification for each employee. The employee_details table serves as the central entity, containing personal information such as name, age, gender, contact details, address, work experience, and employment status.
The emp_designation_promotion table tracks employees' job designations, promotion statuses, and new designations after promotions. The recruitment_type table captures the recruitment mode, associated costs, and skill levels for each employee. The salary_band table maintains the salary grade and corresponding salary for employees. Finally, the training_details table records information about employee training, including training dates, key performance indicators (kpis) before and after training, types of training, training costs, and the number of scheduled training sessions.
These tables are interconnected through foreign key relationships, primarily linking to the employee_code column in the employee_details table, ensuring data integrity and enabling efficient data retrieval and analysis related to employee information across different aspects of human resource management.

[CLICK HERE TO VIEW](https://github.com/jaggaraj/STYLELABS/blob/main/mysql%20stylelabs%20hr.png).

[CLICK HERE TO VIEW](https://github.com/jaggaraj/STYLELABS/blob/main/mysql%20stylelabs_hr%20%20schema.pdf).

# MY SQL DATA BASE FOR BUSINESS OPERATIONS

This document outlines the schema for a mysql database called "stylelabs_operation" designed to manage an e-commerce operation. The schema consists of nine interconnected tables: customer_details, delivery_feedback, hub_details, location_log, mode_of_delivery, mode_of_payment, order_details, product_feedback, and supplier_details.
The customer_details table stores customer information such as customer id, name, age, gender, and account creation date. The order_details table captures order-related data, including customer id, order id, order time, product details, pricing, discounts, quantities, delivery costs, payment id, and supplier id. The mode_of_payment table maintains payment modes, details, and timestamps.
The delivery_feedback table records customer feedback on deliveries, including delivery ratings and reviews. The product_feedback table stores customer reviews and ratings for ordered products, along with images. The hub_details table contains information about delivery hubs, such as hub addresses, delivery personnel, delivery times, delivery types, payment modes, and amounts.
The location_log table tracks customer addresses and mobile numbers for order deliveries. The mode_of_delivery table maintains delivery modes and shipping times for orders. The supplier_details table stores supplier information, including supplier ids, names, and addresses.
These tables are interconnected through foreign key relationships, ensuring data integrity and facilitating efficient data retrieval and analysis related to customer orders, payments, deliveries, feedback, and supplier information.

[CLICK HERE TO VIEW](https://github.com/jaggaraj/STYLELABS/blob/main/mysql%20stylelabs%20operations.png).

[CLICK HERE TO VIEW](https://github.com/jaggaraj/STYLELABS/blob/main/mysql%20stylelabs_operation%20schema.pdf).

# DEVELOPED RECRUITMENT,TRAINING AND DEVELOPMENT POWER BI DASHBOARD FOR STYLE LABS PVT LTD

Training and Development Dashboard includes the following components:
Employee Code and Skill Level filters to select specific employees or skill levels.Cost of Training metric displaying the total cost (104K) of training programs.Trainings Attended metric showing the total number (117) of trainings attended by employees.Scheduled Trainings metric indicating the number (62) of upcoming scheduled training sessions.A bar chart displaying the count of employees with different promotion statuses (Promoted, Not Promoted, and Hold).A bar chart showing the count of promotions across different employee designations.Cost Center and Employee Designation filters to analyze data based on cost centers or job designations.A dual bar chart comparing the sum of kpis (Key Performance Indicators) before and after training, indicating the impact of training on employee performance.A Trainings Schedule Trend line chart showing the trend of scheduled trainings over time (in this case, for the year 2024).Recruitment Type and Education Level filters to analyze data based on recruitment types or educational qualifications.Date filters (Joining Date and Training Date) to filter data based on specific date ranges.
Recruitment Dashboard include:
Total Employees: Shows the total number of employees, which is 67.Cost of Recruitment: Displays the total cost incurred for recruitment, which is 109K.Total Salaries: Indicates the total salaries paid to employees, which is 13M.Employee Diversity: A bar chart showing the gender diversity of employees, with counts for males and females.Working Status: A bar chart depicting the count of employees based on their working status (on-duty or bench).Employees Recruitment Trend: A line chart showing the trend of employee recruitment over three months (Jan 1999, Feb 1999, Mar 1999).Attrition Rate: A blank metric, potentially indicating that attrition rate data is not available or needs to be calculated.Timestamp: Displays the current timestamp, which is 17-05-2024 22:14:18.
The dashboard also includes various filters, such as:
Joining Date: Allows filtering employees based on their joining date range.Emp Code: Enables filtering data based on specific employee codes.Education Level: Filters data based on employees' educational qualifications.Recruitment Type: Allows filtering based on different recruitment types.Salary Grade: Filters data based on employee salary grades.Cost Center: Enables filtering data based on different cost centers.Employee Designation: Allows filtering based on employee job designations.Skill Level: Filters data based on employees' skill levels.

[CLICK HERE TO VIEW](https://app.powerbi.com/view?r=eyJrIjoiNzhjYWYyYjYtMzU0NC00ZTI5LThlZDUtODJlMDE4ZGE5ODlkIiwidCI6IjgwOGNjODNlLWE1NDYtNDdlNy1hMDNmLTczYTFlYmJhMjRmMyIsImMiOjEwfQ%3D%3D)

# DEVELOPED BUSINESS OPERATIONS POWER BI DASHBOARD FOR STYLE LABS PVT LTD

"Style Labs Sales Dashboard" that provides an overview of various sales-related metrics and key performance indicators (kpi’s) for the organization.
The dashboard includes the following key elements:
Sales: Displays the total sales figure, which is 3M.Discount: Shows the total amount of discounts given, which is 267K.No. Of Products Sold: Indicates the total number of products sold, which is 3017.Customers: Displays the total number of customers, which is 797.Delivery Charges: Shows the total delivery charges collected, which is 151K.Order Trend: A line chart displaying the trend of orders placed over time.
The dashboard also includes various filters and slicers, such as:
Mode of Delivery: Allows filtering data based on the mode of delivery (e.g., same-day, express, etc.).Suppliers: Enables filtering data based on specific suppliers.Logistic Firms: Allows filtering data based on the logistic firms involved in delivery.Mode of Payment: Filters data based on the payment modes used by customers.Gender Wise: Allows filtering data based on the gender of customers.Customer ID Wise: Enables filtering data based on specific customer ids.Customer Name Wise: Allows filtering data based on customer names.Order ID Wise: Filters data based on specific order ids.

[CLICK HERE TO VIEW](https://app.powerbi.com/view?r=eyJrIjoiOWI0YTI5MDYtZjRlYS00ZjI3LTk3NDctMDY2ZDY0MjI0OTIxIiwidCI6IjgwOGNjODNlLWE1NDYtNDdlNy1hMDNmLTczYTFlYmJhMjRmMyIsImMiOjEwfQ%3D%3D)

# POWER AUTOMATE FOR JOB APPLICANT PROFILE SCREENING

Start: The process begins when a new response is submitted.
Get Response Details: This step involves gathering information related to the response.
Condition: The process then evaluates profile skill match with required skills. Depending on whether the condition is true or false, it takes different paths:
True Path:
Add a Row into a Table: If the condition is true, a row is added into a selection table.
Send an Email (V2): Following that, an email is sent.
False Path:
Add a Row into Table 1: If the condition is false, a row is added into rejection table.
Send an Email (V2) 1: An email is sent in this case as well.

[CLICK HERE TO VIEW](https://github.com/jaggaraj/STYLELABS/blob/main/hr%20power%20automate.pdf)

# COMBOS AND RECOMMENDATIONS FOR CUSTOMERS WHERE CREATED USING MARKET BASKET ANALYSIS

Based on the data, a strong association exists between SL Custom Joggers-2 and SL Custom Joggers-3. This suggests customers who purchase SL Custom Joggers-2 are also highly likely to buy SL Custom Joggers-3 in the same transaction.Support: 0.0935 - Around 9.35% of transactions contain both joggers styles.
Confidence: High values (0.588 & 0.555): If a customer buys SL Custom Joggers-2, there's a 58.8% or 55.5% chance they'll also purchase SL Custom Joggers-3, depending on the direction of the rule (28 or 29).
Lift: 3.49 - This value is significantly higher than 1, indicating a strong association. Customers are over 3 times more likely to buy both jogger styles together than buying them independently.

[CLICK HERE TO VIEW](https://github.com/jaggaraj/STYLELABS/blob/main/MARKET%20BASKET%20ANALYISIS.pdf)

# PREDICTING EMPLOYEE CHURN 

Each row represents an individual, and the columns are features or attributes related to their performance, experience, and other factors. Here's a brief description of the columns:kpi: Likely stands for Key Performance Indicator, which could be a metric or score quantifying an employee's overall performance.experience: The number of years of experience the employee has.total ratings: Could be an average rating or score for the employee, possibly based on customer or peer feedback.total hikes: The total number of salary or compensation increases received by the employee.no.of promotions: The number of promotions the employee has received.total sales: The total sales volume or revenue generated by the employee (applicable for sales roles).total salary: The total salary or compensation received by the employee.total working hours: The total number of working hours logged by the employee.no.of trainings: The number of training programs or sessions the employee has attended.no.of stress relief program: The number of stress relief or wellness programs the employee has participated in.turn over: This could be a binary indicator (1 or 2) representing whether the employee has left the organization (turned over) or not.random forest model got 65 accuracy it can predict the employee turnover.

[CLICK HERE TO VIEW](https://github.com/jaggaraj/STYLELABS/blob/main/Untitled2.ipynb)

#  DATA CLEANING

imports the necessary libraries: pandas for data manipulation, numpy for numerical operations, and 
ydata_profiling for generating a profile report of the dataset.

The ProfileReport function from the ydata_profiling library is called on the dt DataFrame to generate a descriptive report of the dataset.
The code then displays the entire dt DataFrame.
The dt['marks'] column is cleaned by removing certain special characters (!#$%@}{][|^&''""*^)()) from each entry using the str.strip() method.
Similarly, the dt['name'] column is cleaned by removing special characters and digits from each entry using str.strip().
The DataFrame is then truncated to include only the first 20 rows using dt = dt.iloc[:20].
Any missing values (NaN) in the DataFrame are filled with an empty string ' ' using dt = dt.fillna(' ').
Finally, the cleaned and processed DataFrame dt is displayed.

[CLICK HERE TO VIEW](https://github.com/jaggaraj/STYLELABS/blob/main/Untitled10.ipynb)

# FORECASTING SALES 

Output provided is a univarient time series analysis ARIMA (Autoregressive Integrated Moving Average) model in R. It shows the point forecasts and prediction intervals for future time periods.For January 2012, there is an 80% probability that the true value will fall between 10.225423 and 11.71738.For January 2012, there is a 95% probability that the true value will fall between 9.830527 and 12.11227.

[CLICK HERE TO VIEW](https://github.com/jaggaraj/STYLELABS/blob/main/arima.pdf)

code for using the Prophet library in R for time series forecasting. Prophet is an open-source library developed by Facebook's Core Data Science team for forecasting time series data based on an additive model where non-linear trends are fit with yearly, weekly, and daily seasonality, plus holiday effects.output suggests there will be downward trend 

[CLICK HERE TO VIEW](https://github.com/jaggaraj/STYLELABS/blob/main/prophet%20by%20facebook.pdf)

[CLICK HERE TO VIEW](file:///C:/Users/Dell/Documents/tgf.html)



![Green Pink Multicolor Fashion Brand Photo Collage LinkedIn Background Photo](https://github.com/jaggaraj/STYLELABS/assets/123171411/99007dbd-fbf5-4e88-b941-169a7b730edf)


![White Hand Drawn simple Coming Soon Instagram Post](https://github.com/jaggaraj/STYLELABS/assets/123171411/b2e24960-5024-406c-9bfe-5168e551f2d6) 

