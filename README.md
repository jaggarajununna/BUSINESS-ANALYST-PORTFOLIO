# STYLELABS
IMPLEMENING CERTAIN DATA STORAGE AND DATA ANALYSIS TECHNOLOGIES AT STYLE LABS PVT LTD.

# INTRODUCTION
Style labs is primarily focused on providing clients with high-quality designer clothing. They put a lot of effort into creating unique, superior designs that satisfy a range of stylistic preferences. As its business grows, the company is thinking about making decisions based on data, and it has begun implementing certain data storage and data analysis technologies.

# PROBLEMS
DATA STORAGE

POWER BI DASHBOARDS

DESIGNING OF COMBOS

POWER AUTOMATE FOR HR SCREENING PROCESS

DATA DRIVEN DECISION MAKING

 # TOOLS USED
 MY SQL
 
 MS OFFICE
 
 PYTHON
 
 R-PROGRAMME
 
 POWER AUTOMATE
 
 VISIO
 
 POWER BI

# DEVELOPED MYSQL DATABASE FOR STYLE LABS PVT LTD

   ## MY SQL DATA BASE FOR HUMAN RESOURCES MANAGEMENT OPERATION
   
The provided document presents the schema for a mysql database named "stylelabs_hr" designed to store and manage employee-related information. The schema consists of seven interconnected tables: cost_center, education_details, employee_details, emp_designation_promotion, recruitment_type, salary_band, and training_details.
The cost_center table stores details about the employee's cost center, including the employee code, strategic business unit (sbu) address, and joining date. The education_details table records the highest educational qualification for each employee. The employee_details table serves as the central entity, containing personal information such as name, age, gender, contact details, address, work experience, and employment status.
The emp_designation_promotion table tracks employees' job designations, promotion statuses, and new designations after promotions. The recruitment_type table captures the recruitment mode, associated costs, and skill levels for each employee. The salary_band table maintains the salary grade and corresponding salary for employees. Finally, the training_details table records information about employee training, including training dates, key performance indicators (kpis) before and after training, types of training, training costs, and the number of scheduled training sessions.
These tables are interconnected through foreign key relationships, primarily linking to the employee_code column in the employee_details table, ensuring data integrity and enabling efficient data retrieval and analysis related to employee information across different aspects of human resource management.


[VIEW HRM ER DIAGRAM](https://github.com/jaggaraj/STYLELABS/blob/main/mysql%20stylelabs%20hr.png).

[VIEW HRM DATABASE SCHEMA](https://github.com/jaggaraj/STYLELABS/blob/main/mysql%20stylelabs_hr%20%20schema.pdf).

  ## MY SQL DATA BASE FOR BUSINESS OPERATIONS

The provided document outlines the schema for a mysql database called "stylelabs_operation" designed to manage an e-commerce operation. The schema consists of nine interconnected tables: customer_details, delivery_feedback, hub_details, location_log, mode_of_delivery, mode_of_payment, order_details, product_feedback, and supplier_details.
The customer_details table stores customer information such as customer id, name, age, gender, and account creation date. The order_details table captures order-related data, including customer id, order id, order time, product details, pricing, discounts, quantities, delivery costs, payment id, and supplier id. The mode_of_payment table maintains payment modes, details, and timestamps.
The delivery_feedback table records customer feedback on deliveries, including delivery ratings and reviews. The product_feedback table stores customer reviews and ratings for ordered products, along with images. The hub_details table contains information about delivery hubs, such as hub addresses, delivery personnel, delivery times, delivery types, payment modes, and amounts.
The location_log table tracks customer addresses and mobile numbers for order deliveries. The mode_of_delivery table maintains delivery modes and shipping times for orders. The supplier_details table stores supplier information, including supplier ids, names, and addresses.
These tables are interconnected through foreign key relationships, ensuring data integrity and facilitating efficient data retrieval and analysis related to customer orders, payments, deliveries, feedback, and supplier information.


[VIEW BUSINESS OPERATIONS ER DIAGRAM](https://github.com/jaggaraj/STYLELABS/blob/main/mysql%20stylelabs%20operations.png).

[VIEW BUSINESS OPERATIONS DATABASE SCHEMA](https://github.com/jaggaraj/STYLELABS/blob/main/mysql%20stylelabs_operation%20schema.pdf).

# DEVELOPED RECRUITMENT,TRAINING AND DEVELOPMENT POWER BI DASHBOARD FOR STYLE LABS PVT LTD

Training and Development Dashboard includes the following components:
Employee Code and Skill Level filters to select specific employees or skill levels.Cost of Training metric displaying the total cost (104K) of training programs.Trainings Attended metric showing the total number (117) of trainings attended by employees.Scheduled Trainings metric indicating the number (62) of upcoming scheduled training sessions.A bar chart displaying the count of employees with different promotion statuses (Promoted, Not Promoted, and Hold).A bar chart showing the count of promotions across different employee designations.Cost Center and Employee Designation filters to analyze data based on cost centers or job designations.A dual bar chart comparing the sum of kpis (Key Performance Indicators) before and after training, indicating the impact of training on employee performance.A Trainings Schedule Trend line chart showing the trend of scheduled trainings over time (in this case, for the year 2024).Recruitment Type and Education Level filters to analyze data based on recruitment types or educational qualifications.Date filters (Joining Date and Training Date) to filter data based on specific date ranges.
Recruitment Dashboard include:
Total Employees: Shows the total number of employees, which is 67.Cost of Recruitment: Displays the total cost incurred for recruitment, which is 109K.Total Salaries: Indicates the total salaries paid to employees, which is 13M.Employee Diversity: A bar chart showing the gender diversity of employees, with counts for males and females.Working Status: A bar chart depicting the count of employees based on their working status (on-duty or bench).Employees Recruitment Trend: A line chart showing the trend of employee recruitment over three months (Jan 1999, Feb 1999, Mar 1999).Attrition Rate: A blank metric, potentially indicating that attrition rate data is not available or needs to be calculated.Timestamp: Displays the current timestamp, which is 17-05-2024 22:14:18.
The dashboard also includes various filters, such as:
Joining Date: Allows filtering employees based on their joining date range.Emp Code: Enables filtering data based on specific employee codes.Education Level: Filters data based on employees' educational qualifications.Recruitment Type: Allows filtering based on different recruitment types.Salary Grade: Filters data based on employee salary grades.Cost Center: Enables filtering data based on different cost centers.Employee Designation: Allows filtering based on employee job designations.Skill Level: Filters data based on employees' skill levels.

[VIEW HRM POWER BI DASHBOARD](https://github.com/jaggaraj/STYLELABS/blob/main/POWER%20BI%20HRM%20PDF.pdf)

# DEVELOPED BUSINESS OPERATIONS POWER BI DASHBOARD FOR STYLE LABS PVT LTD

"Style Labs Sales Dashboard" that provides an overview of various sales-related metrics and key performance indicators (kpi’s) for the organization.
The dashboard includes the following key elements:
Sales: Displays the total sales figure, which is 3M.Discount: Shows the total amount of discounts given, which is 267K.No. Of Products Sold: Indicates the total number of products sold, which is 3017.Customers: Displays the total number of customers, which is 797.Delivery Charges: Shows the total delivery charges collected, which is 151K.Order Trend: A line chart displaying the trend of orders placed over time.
The dashboard also includes various filters and slicers, such as:
Mode of Delivery: Allows filtering data based on the mode of delivery (e.g., same-day, express, etc.).Suppliers: Enables filtering data based on specific suppliers.Logistic Firms: Allows filtering data based on the logistic firms involved in delivery.Mode of Payment: Filters data based on the payment modes used by customers.Gender Wise: Allows filtering data based on the gender of customers.Customer ID Wise: Enables filtering data based on specific customer ids.Customer Name Wise: Allows filtering data based on customer names.Order ID Wise: Filters data based on specific order ids.

[VIEW OPERATION POWER BI DASHBOARD](https://github.com/jaggaraj/STYLELABS/blob/main/POWER%20BI%20OPERATIONS%20PDF.pdf)

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

[VIEW POWER AUTOMATION](https://github.com/jaggaraj/STYLELABS/blob/main/hr%20power%20automate.pdf)

# COMBOS AND RECOMMENDATIONS FOR CUSTOMERS WHERE CREATED USING MARKET BASKET ANALYSIS

Based on the data, a strong association exists between SL Custom Joggers-2 and SL Custom Joggers-3. This suggests customers who purchase SL Custom Joggers-2 are also highly likely to buy SL Custom Joggers-3 in the same transaction.Support: 0.0935 - Around 9.35% of transactions contain both joggers styles.
Confidence: High values (0.588 & 0.555): If a customer buys SL Custom Joggers-2, there's a 58.8% or 55.5% chance they'll also purchase SL Custom Joggers-3, depending on the direction of the rule (28 or 29).
Lift: 3.49 - This value is significantly higher than 1, indicating a strong association. Customers are over 3 times more likely to buy both jogger styles together than buying them independently.

