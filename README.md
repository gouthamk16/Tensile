# Tensile
Data analysis and process optimization tool designed specifically for logisitics and supply chain management. Enabling businesses to analyze real-time and historical logistics data, identify inefficiencies, and implement AI-driven workflows for operational improvement and streamlined supply chain operations.

## Features
- Demand Forecasting
- Inventory optimization
- Route plannning and Optimization
- Predictive analytics
- Recommendations for operational improvements, risk mitigation, and cost reduction

## MVP
- Data ingestion pipeline
- Route optimization
- Inventory management with demand forecasting
- A data visualization dashboard to display real time data and results of the analysis.

## Research
- The data (How is the data collected? How is it stored? Processing requirements, ingestion pipelines, etc.)
- How can data from mutliple sources be integrated to form one single source of truth?
- The analysis (What kind of analysis is performed? What are the outputs? What are the tools, algorithms used?)
- Predictive analytics. Finding patterns in the data.
- Optimization algorithms. Output from data analysis to suggestions for process optimization.
- Integrating AI into the system. Learning patterns to providing suggestions for supply-chain management and generating reports.
- Laying out the outputs. How will the outputs be presented to the user? What kind of visualizations will be used?
- How will the user interact with the system? 
- Data security

## Roadmap
- Data ingestion pipeline
    - Ingesting data from S3.
    - Interpret data as an excel file for now.
- Create a simple visualization tool for https://brunel.figshare.com/articles/dataset/Supply_Chain_Logistics_Problem_Dataset/7558679?file=20162015
    - Cost visualization for the tab "Freight Rates"
    - Find the most efficient carrier type using the "FreightRates" tab.
    - Efficiency of each plant from the "WhCosts" and "WhCapacities" tab.
