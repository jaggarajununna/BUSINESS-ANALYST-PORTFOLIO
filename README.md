# STYLELABS
IMPLEMENING CERTAIN DATA STORAGE AND DATA ANALYSIS TECHNOLOGIES AT STYLE LABS PVT LTD.

# INTRODUCTION
STYLE LABS IS PRIMARILY FOCUSED ON PROVIDING CLIENTS WITH HIGH-QUALITY DESIGNER CLOTHING. THEY PUT A LOT OF EFFORT INTO CREATING UNIQUE, SUPERIOR DESIGNS THAT SATISFY A RANGE OF STYLISTIC PREFERENCES. AS ITS BUSINESS GROWS, THE COMPANY IS THINKING ABOUT MAKING DECISIONS BASED ON DATA, AND IT HAS BEGUN IMPLEMENTING CERTAIN DATA STORAGE AND DATA ANALYSIS TECHNOLOGIES.

# PROBLEMS
DATA STORAGE

POWER BI DASHBOARDS

DESIGNING OF COMBOS

POWER AUTOMATE FOR HR SCREENING PROCESS

DATA DRIVEN DECISION MAKING

 # TOOLS USED
 MY SQL.
 MS OFFICE.
 PYTHON.
 R-PROGRAMME.
 POWER AUTOMATE.
 VISIO.
 POWER BI.

# DEVELOPED MYSQL DATABASE FOR STYLE LABS PVT LTD

   ## MY SQL DATA BASE FOR HUMAN RESOURCES MANAGEMENT OPERATION
   
The provided document presents the schema for a mysql database named "stylelabs_hr" designed to store and manage employee-related information. The schema consists of seven interconnected tables: cost_center, education_details, employee_details, emp_designation_promotion, recruitment_type, salary_band, and training_details.
The cost_center table stores details about the employee's cost center, including the employee code, strategic business unit (sbu) address, and joining date. The education_details table records the highest educational qualification for each employee. The employee_details table serves as the central entity, containing personal information such as name, age, gender, contact details, address, work experience, and employment status.
The emp_designation_promotion table tracks employees' job designations, promotion statuses, and new designations after promotions. The recruitment_type table captures the recruitment mode, associated costs, and skill levels for each employee. The salary_band table maintains the salary grade and corresponding salary for employees. Finally, the training_details table records information about employee training, including training dates, key performance indicators (kpis) before and after training, types of training, training costs, and the number of scheduled training sessions.
These tables are interconnected through foreign key relationships, primarily linking to the employee_code column in the employee_details table, ensuring data integrity and enabling efficient data retrieval and analysis related to employee information across different aspects of human resource management.


[VIEW HRM ER DIAGRAM](https://github.com/jaggaraj/STYLELABS/blob/main/mysql%20stylelabs%20hr.png).

[VIEW HRM DATABASE SCHEMA](https://github.com/jaggaraj/STYLELABS/blob/main/mysql%20stylelabs_hr%20%20schema.pdf).

  ## MY SQL DATA BASE FOR BUSINESS OPERATIONS

the provided document outlines the schema for a mysql database called "stylelabs_operation" designed to manage an e-commerce operation. the schema consists of nine interconnected tables: customer_details, delivery_feedback, hub_details, location_log, mode_of_delivery, mode_of_payment, order_details, product_feedback, and supplier_details.
the customer_details table stores customer information such as customer id, name, age, gender, and account creation date. the order_details table captures order-related data, including customer id, order id, order time, product details, pricing, discounts, quantities, delivery costs, payment id, and supplier id. the mode_of_payment table maintains payment modes, details, and timestamps.
the delivery_feedback table records customer feedback on deliveries, including delivery ratings and reviews. the product_feedback table stores customer reviews and ratings for ordered products, along with images. the hub_details table contains information about delivery hubs, such as hub addresses, delivery personnel, delivery times, delivery types, payment modes, and amounts.
the location_log table tracks customer addresses and mobile numbers for order deliveries. the mode_of_delivery table maintains delivery modes and shipping times for orders. the supplier_details table stores supplier information, including supplier ids, names, and addresses.
these tables are interconnected through foreign key relationships, ensuring data integrity and facilitating efficient data retrieval and analysis related to customer orders, payments, deliveries, feedback, and supplier information.


[VIEW BUSINESS OPERATIONS ER DIAGRAM](https://github.com/jaggaraj/STYLELABS/blob/main/mysql%20stylelabs%20operations.png).

[VIEW BUSINESS OPERATIONS DATABASE SCHEMA](https://github.com/jaggaraj/STYLELABS/blob/main/mysql%20stylelabs_operation%20schema.pdf).
