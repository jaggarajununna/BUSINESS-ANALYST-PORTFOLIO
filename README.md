![Green Pink Multicolor Fashion Brand Photo Collage LinkedIn Background Photo](https://github.com/jaggaraj/STYLELABS/assets/123171411/99007dbd-fbf5-4e88-b941-169a7b730edf)

IMPLEMENING CERTAIN DATA STORAGE AND DATA ANALYSIS TECHNOLOGIES AT STYLE LABS PVT LTD.

#  INTRODUCTION
Style labs is primarily focused on providing clients with high-quality designer clothing. They put a lot of effort into creating unique, superior designs that satisfy a range of stylistic preferences. As its business grows, the company is thinking about making decisions based on data, and it has begun implementing certain data storage and data analysis technologies.


#  TOOLS

 ![R](https://github.com/jaggarajununna/STYLELABS/assets/123171411/19c06d87-d0ea-472b-9528-84a28580775a)


 
[SEGMENTATION OF CUSTOMERS](https://github.com/jaggaraj/STYLELABS/blob/main/CLUSTER%20ANALYSIS.pdf) 

![VIEW](https://github.com/jaggarajununna/PORTFOLIO/blob/main/Segmentation.jpg)

The 100 responses were categorized into two groups using k-modes clustering, based on age, salary, event, and preferences. Cluster 1 included individuals aged 36-45 with over $100,000 per year, attending festivals, and preferring trendy styles, while Cluster 2 included those aged 26-35 with over $50,000 per year, attending dates, and preferring casual styles.
 

[HUMAN RESOURCES MANAGEMENT DATABASE](https://github.com/jaggaraj/STYLELABS/blob/main/mysql%20stylelabs%20hr.png)


![VIEW](https://github.com/jaggarajununna/PORTFOLIO/blob/main/OIP.jpeg)
   
The document presents a schema for a MySQL database called "stylelabs_hr" that manages employee-related information. It consists of seven interconnected tables: cost_center, education_details, employee_details, emp_designation_promotion, recruitment_type, salary_band, and training_details. These tables store employee information, such as cost center, education, and training. The schema is interconnected through foreign key relationships, ensuring data integrity and efficient data retrieval and analysis across various aspects of human resource management.



[BUSINESS OPERATIONS DATABASE](https://github.com/jaggaraj/STYLELABS/blob/main/mysql%20stylelabs%20operations.png)

The "stylelabs_operation" database schema is a MySQL database for managing an e-commerce operation. It comprises nine interconnected tables: customer_details, delivery_feedback, hub_details, location_log, mode_of_delivery, mode_of_payment, order_details, product_feedback, and supplier_details. These tables store customer information, order-related data, payment modes, delivery feedback, product feedback, hub details, location_log, mode_of_delivery, and supplier details. The tables are interconnected through foreign key relationships for efficient data retrieval and analysis.


[HUMAN RESOURCES MANAGEMENT DASHBOARD](https://app.powerbi.com/viewr=eyJrIjoiODE5NWZjZDQtNDU0MC00ZTY4LTgzMzYtOTliMDI5NDg4MGI5IiwidCI6IjgwOGNjODNlLWE1NDYtNDdlNy1hMDNmLTczYTFlYmJhMjRmMyIsImMiOjEwfQ%3D%3D)

![VIEW](https://github.com/jaggarajununna/PORTFOLIO/blob/main/Sales-YTD-dashboard-example-1efebb.png)

The Training and Development Dashboard is a comprehensive tool for tracking employee performance and training costs. It includes filters for employee code and skill level, total training attendance, scheduled training sessions, promotion statuses, cost centers, job designations, and performance indicators. The dashboard also shows the trend of scheduled trainings over time, recruitment types and education levels, and date ranges. The recruitment dashboard shows the total number of employees, cost of recruitment, salaries, gender diversity, working status, recruitment trends, attrition rate, and current timestamp. Filters include joining date, employee codes, education level, recruitment type, salary grades, cost centers, job designations, and skill levels.


[BUSINESS OPERATIONS DASHBOARD](https://app.powerbi.com/view?r=eyJrIjoiODM4NmIzNjctMTFhOC00YWIxLWE0MzYtZjdhYTQ0ZGI5OWViIiwidCI6IjgwOGNjODNlLWE1NDYtNDdlNy1hMDNmLTczYTFlYmJhMjRmMyIsImMiOjEwfQ%3D%3D)

The "Style Labs Sales Dashboard" provides an overview of sales metrics and key performance indicators for an organization. It includes sales, discounts, product sales, customers, delivery charges, and order trends. The dashboard also includes filters and slicers for delivery mode, suppliers, logistic firms, payment modes, gender, customer ID, customer name, and order ID. The data is organized by order ID.



[ATS](https://github.com/jaggaraj/STYLELABS/blob/main/hr%20power%20automate.pdf)

Start: The process begins when a new response is submitted.
Get Response Details: This step involves gathering information related to the response.
Condition: The process then evaluates profile skill match with required skills. Depending on whether the condition is true or false, it takes different paths:
True Path:
Add a Row into a Table: If the condition is true, a row is added into a selection table.
Send an Email (V2): Following that, an email is sent.
False Path:
Add a Row into Table 1: If the condition is false, a row is added into rejection table.
Send an Email (V2) 1: An email is sent in this case as well.



[MARKET BASKET ANALYSIS](https://github.com/jaggaraj/STYLELABS/blob/main/MARKET%20BASKET%20ANALYISIS.pdf)

![VIEW](https://github.com/jaggarajununna/PORTFOLIO/blob/main/13952Market-basket-analysis.png)

Based on the data, a strong association exists between SL Custom Joggers-2 and SL Custom Joggers-3. This suggests customers who purchase SL Custom Joggers-2 are also highly likely to buy SL Custom Joggers-3 in the same transaction.Support: 0.0935 - Around 9.35% of transactions contain both joggers styles.
Confidence: High values (0.588 & 0.555): If a customer buys SL Custom Joggers-2, there's a 58.8% or 55.5% chance they'll also purchase SL Custom Joggers-3, depending on the direction of the rule (28 or 29).
Lift: 3.49 - This value is significantly higher than 1, indicating a strong association. Customers are over 3 times more likely to buy both jogger styles together than buying them independently.



[PREDICTING EMPLOYEE CHURN](https://github.com/jaggaraj/STYLELABS/blob/main/Untitled2.ipynb)

![VIEW](https://github.com/jaggarajununna/PORTFOLIO/blob/main/What-Is-Machine-Learning1.jpg)

Each row represents an individual, and the columns are features or attributes related to their performance, experience, and other factors. Here's a brief description of the columns:kpi: Likely stands for Key Performance Indicator, which could be a metric or score quantifying an employee's overall performance.experience: The number of years of experience the employee has.total ratings: Could be an average rating or score for the employee, possibly based on customer or peer feedback.total hikes: The total number of salary or compensation increases received by the employee.no.of promotions: The number of promotions the employee has received.total sales: The total sales volume or revenue generated by the employee (applicable for sales roles).total salary: The total salary or compensation received by the employee.total working hours: The total number of working hours logged by the employee.no.of trainings: The number of training programs or sessions the employee has attended.no.of stress relief program: The number of stress relief or wellness programs the employee has participated in.turn over: This could be a binary indicator (1 or 2) representing whether the employee has left the organization (turned over) or not.random forest model got 65 accuracy it can predict the employee turnover.



[SALES FORECASTING](https://github.com/jaggaraj/STYLELABS/blob/main/prophet%20by%20facebook.pdf)

![VIEW](https://github.com/jaggarajununna/PORTFOLIO/blob/main/OIP%20(1).jpeg)


code for using the Prophet library in R for time series forecasting. Prophet is an open-source library developed by Facebook's Core Data Science team for forecasting time series data based on an additive model where non-linear trends are fit with yearly, weekly, and daily seasonality, plus holiday effects.output suggests there will be downward trend 

