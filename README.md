# Task003-ML-DL-Rec-Sys-Course-20231201
Recommender System Supervised and Unsupervised Learning

# Objectives
​
Course4U grows rapidly and reaches millions of learners in a very short period. The learning topics of AI Training Room can be summarized in the following word cloud:

<center>
    <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-ML321EN-SkillsNetwork/labs/module_1/images/word_cloud.png" width="600" alt="word cloud">
<center>

Starting this year, machine learning engineer team is working very hard on a recommender system project. **The main goal of this project is to improve learners’ learning experience via helping them quickly find new interested courses and better paving their learning paths**. Meanwhile, **with more learners interacting with more courses via C4U recommender systems,C4U company’s revenue may also be increased**.

This project is currently at the *Proof of Concept (PoC) phase* so your **main focus at this moment is to explore and compare various machine learning models and find one with the best performance in off-line evaluations.**

In  <a href="https://www.kaggle.com/code/wahyuardhitama/task003-p001-ml-dl-rec-sys-course-20231025">part 1 (P01)</a>, we elaborate on a content-based recommender system using unsupervised learning, where we utilize user profiles and course genres. In <a href="https://www.kaggle.com/wahyuardhitama/task003-p002-ml-dl-rec-sys-course-20231029">part 2 (P02)</a>, we explore clustering-based recommender system using unsupervised learning. Finally, in the last part,<a href="https://www.kaggle.com/wahyuardhitama/task003-p003-ml-dl-rec-sys-course-20231101"> part 3 (P03)</a>, we take a deep dive into a content-based recommender system using supervised learning. All documents are available in the <a href="https://github.com/whyzie/Task003-ML-DL-Rec-Sys-Course-20231201">Github.</a>

### Note: 
This project's dataset was created for pedagogical purposes and may not represent real-world data. The project consists of multiple notebook parts, focusing on combining data from various tables and conducting data analysis and prediction to acquire valuable insights.

<h3 style = "text-align:center">Table 1.1. Project Charter</h3>
<table style="color:black;
           display:fill;
           border-colapse: colapse;
           width: 100%;
           border: 1px solid black;
           border-collapse: collapse;
           border-style: solid;
           border-radius:5px;
           background-color:#5642C5;
           font-size:110%;
           font-family:Verdana;
           letter-spacing:0.5px">
  
  <tr>
    <th colspan ="4" style="text-align:center">Project Recommender System</th>
  </tr>
    <tr>
    <th colspan ="4" style="text-align:center">25th Oct 2023</th>
  </tr>
  <tr>
      <th colspan ="4" style="text-align:center">Document Status: <del>Draft</del> | In Review | <del>Approved</del></th>
  </tr>
  <tr>
      <th colspan ="4" style="text-align:center">Executive Summary</th>
  </tr>
  <tr>
      <td colspan ="4" style="text-align:center">Explore and compare  various machine learning models and find one with                                         to improve learners’ learning experience.</td>
  </tr>
  <tr style ="background:LightSkyBlue;text-align:center">
      <td colspan ="2">Business Case</td>
      <td colspan ="2">Problem/Opportunity Statement</td>
  </tr>
 <tr style="text-align:left">
     <td colspan ="2">Course4U growing , having reached ~34,000 users and over 233,000 enrollments in a year.</td>
     <td colspan ="2">
         <ul>
         <li>25,000 users (70%) who have enrolled in fewer than 10 courses.
         <li>Among them, 8,000 users have enrolled in only a single course. 
         <li>Only less than 45% of the total courses have been chosen by users.
         <li>Encourage existing users to enroll in more than 10 courses. 
         <li>Increase in new users year to year.
     </ul> 
</td>  
  </tr>

 <tr style ="background:LightSkyBlue;text-align:center">
      <td colspan ="2">Goal Statement</td>
      <td colspan ="2">Deliverables (Key Results)</td>
 </tr>
 <tr style="text-align:left">
      <td colspan ="2">
Maximize user engagement, increase revenue streams, and solidify Course4U's position in the online education market.
257,500 enrollments next year.
<p>Primary metric:
     <ul>
         <li>Number of enrollments
     </ul>
     Secondary Metric:
     <ul>
         <li>Courses enrolled in the list from 45% to > 50%
         <li>New Users increase 10%
     </ul>
     </td>
      <td colspan ="2">Primary Key Results:
     <ul>
         <li>Increase course enrollment by 10%
     </ul>
     Secondary Key Results:
     <ul>
         <li>% courses from the list
         <li>% Incremental increase
     </ul>
     </td>
  </tr>
 
 <tr style ="background:LightSkyBlue;text-align:center">
      <td colspan ="2">Benefits, Cost, and Budget</td>
      <td colspan ="2">Scope and Exclusion</td>
 </tr>
 <tr style="text-align:left">
      <td colspan ="2">Benefits:
     <ul>
         <li>Increase revenue
         <li>Customer engagements (Users and New Users)
     </ul>
     Costs:
     <ul>
         <li>Machine learning's recommender system implementation
         <li>Conversion campaign 
         <li>Tracked via online conversions and mobile - SDK
     </ul>
     Budget Needed:
           <span>TBD</span>
     </td>
      <td colspan ="2">In-Scope:
     <ul>
         <li>Current courses
         <li>Online only
     </ul>
     Out-of-Scope:
     <ul>
         <li>Offline
     </ul>
     </td>
  </tr>   
 
 <tr style ="background:LightSkyBlue;text-align:center">
      <td colspan ="2">Project Team</td>
      <td colspan ="2">Measuring Success</td>
 </tr>
 <tr style="text-align:left">
      <td colspan ="2"> 
     <ul>
         <li>Sponsor: Jamal Harris, Director, Customer Data
         <li>Owner: Sara Romero, VP, Marketing and Ernest Cox, VP, Product Development
         <li>Leader: Wahyu Ardhitama, Head of Data Analytics
         <li>Member: Nina Locklear, Director, Procurement, Adhira Patel, API Strategist, Megan Pirato, Data Warehousing Specialist, Rick Andersson, Manager, Data Governance, Tessa Blackwell, Data Analyst, Brianne Sand, Director, IT and Shareefah Hakimi, Project Manager
     </ul>
     </td>
  
  <td colspan ="2">Deliverables after solutions implementation:
     <ul>Recommender system delivers more incremental value of enrollments relative to the current systems.
         <li>Quickly find new interested courses
         <li>Better paving learning paths
         <li>More learners interacting with more courses
     </ul>
  </td>
  </tr>
  </table>

# Conclussion
We have built collaborative-filtering recommender system models  using supervised learning. 

To determine the best recommender system based on the RMSE data provided, we need to choose the model with the lowest RMSE value because RMSE measures the average deviation of predicted values from actual values. The lower the RMSE, the better the model's performance in terms of accuracy.

<ul>Based on the given the models and RMSE values:
<li>BaggingClassifier: 0.127622
<li>GradientBoostingClassifier: 0.158144
<li>DecisionTreeClassifier: 0.196842
<li>NMF: 0.196469
<li>KNN: 0.190511
<li>LogisticRegression: 0.213301
<li>SVC: 0.213301
<li>NMF_clf: 0.242589
<li>KNN_clf: 0.242589
<li>NN: 0.534776
<li>NN_1: 0.534776
<li>Regression: 0.996619
</ul>
<hr>

<div class="alert alert-block alert-success" style="font-family:verdana; font-size:14px">
<ol>The Result
    <li>The BaggingClassifier has the lowest RMSE (0.127622), indicating better performance in predicting ratings or recommendations among the provided models.
    <li>From the provided list, models such as DecisionTreeClassifier (RMSE: 0.196842) and BaggingClassifier (RMSE: 0.127622) are typically less computationally expensive compared to neural network models like NN and NN_1 (RMSE: 0.534776).
    <li>If you're exploring the structure or patterns within the data without labeled examples, unsupervised learning is more appropriate. It can help in understanding the underlying structure of the data and finding hidden patterns.
    <li>Unsupervised learning algorithms like k-means clustering can be useful for segmenting data into distinct groups based on similarities.
    <li>Techniques like Principal Component Analysis (PCA) or t-distributed Stochastic Neighbor Embedding (t-SNE) are used for dimensionality reduction and visualization, which can be valuable for understanding high-dimensional data.
     <li>Unsupervised learning is often used for anomaly detection where the goal is to identify rare events or outliers in the data.
     <li>If you have a sufficient amount of labeled data, supervised learning models can be a good choice. For example, in classification or regression tasks where you have labeled examples of input-output pairs, supervised learning can be effective.
     <li>When the objective is well-defined and can be framed as predicting an outcome based on input features, supervised learning is suitable. For example, predicting customer churn, spam detection, sentiment analysis, etc.
     <li>Supervised learning models are evaluated based on metrics like accuracy, precision, recall, F1-score, etc., which make it easier to assess model performance.
     <li>Sometimes, a combination of supervised and unsupervised learning techniques is used, known as semi-supervised learning. This can be beneficial when labeled data is limited but unlabeled data is abundant.

</ol>
  
