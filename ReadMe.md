
HEROES OF PYMOLI DATA ANALYSIS


```python
import pandas as pd
import numpy as np

items_complete = "generated_data/items_complete.csv"
players_complete = "generated_data/players_complete.csv"
purchase_complete = "generated_data/Purchase_data_3.csv"
json_file = "HeroesOfPymoli/purchase_data.json"

players_df = pd.read_csv(players_complete)
items_df = pd.read_csv(items_complete)
purchase_df = pd.read_csv(purchase_complete)
purchase_data = pd.read_json(json_file, orient="records")
```

PLAYER COUNT


```python
#Player Count
player_pop = int(players_df["Player ID"].nunique())
player_count_df = pd.DataFrame({"Total Players": [player_pop]}) 
player_count_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1163</td>
    </tr>
  </tbody>
</table>
</div>



PURCHASING ANALYSIS (TOTAL)


```python
unique_items = int(items_df["Item Name"].nunique())
average_price = float(purchase_df["Price"].mean()) 
total_purchases = int(purchase_df["Purchase ID"].count())
total_revenue = float(purchase_df["Price"].sum())

purchasing_analysis_total = pd.DataFrame({
    "Number of Unique Items": [unique_items],
    "Average Purchase Price": [average_price],
    "Total Number of Purchases": [total_purchases],
    "Total Revenue": [total_revenue]}, columns =["Number of Unique Items",
                                                  "Average Purchase Price",
                                                 "Total Number of Purchases",
                                                 "Total Revenue"])
purchasing_analysis_total["Average Purchase Price"] = purchasing_analysis_total["Average Purchase Price"].map("${:.2f}".format)
purchasing_analysis_total["Total Revenue"] = purchasing_analysis_total["Total Revenue"].map("${:.2f}".format)
purchasing_analysis_total
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Number of Unique Items</th>
      <th>Average Purchase Price</th>
      <th>Total Number of Purchases</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>186</td>
      <td>$2.92</td>
      <td>78</td>
      <td>$228.10</td>
    </tr>
  </tbody>
</table>
</div>



GENDER DEMOGRAPHICS


```python
only_genders = players_df.loc[(players_df["Gender"] =="Male") | 
                              (players_df["Gender"] =="Female") | 
                              (players_df["Gender"] =="Other / Non-Disclosed")]
total_pop = only_genders["Gender"].count()

only_male = players_df.loc[players_df["Gender"] == "Male", :]
male_pop = only_male["Gender"].count()

only_female = players_df.loc[players_df["Gender"] == "Female", :]
female_pop = only_female["Gender"].count()

only_other = players_df.loc[players_df["Gender"] == "Other / Non-Disclosed", :]
other_pop = only_other["Gender"].count()

male_percent = round(male_pop / total_pop * 100, 2)
female_percent = round(female_pop / total_pop *100, 2)
other_percent = round(other_pop / total_pop *100, 2)

gender_demographics_total = pd.DataFrame({
    "Gender": ["Male", "Female", "Other / Non-Disclosed"],
    "Percentage of Players": [male_percent,female_percent, other_percent],
    "Total Count": [male_pop, female_pop, other_pop]}, columns=['Gender',
                                                               "Percentage of Players",
                                                               "Total Count"])
gender_demographics_total
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Gender</th>
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Male</td>
      <td>82.03</td>
      <td>954</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Female</td>
      <td>16.08</td>
      <td>187</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Other / Non-Disclosed</td>
      <td>1.89</td>
      <td>22</td>
    </tr>
  </tbody>
</table>
</div>



PURCHASING ANALYSIS (GENDER)


```python
all_purchase = purchase_df.loc[(purchase_df["Gender"] =="Male") | 
                              (purchase_df["Gender"] =="Female") | 
                              (purchase_df["Gender"] =="Other / Non-Disclosed")]
total_purchase = all_purchase["Gender"].count()

male_purchase = purchase_df.loc[purchase_df["Gender"] == "Male", :]
male_purch = male_purchase["Gender"].count()

female_purchase = purchase_df.loc[purchase_df["Gender"] == "Female", :]
female_purch = female_purchase["Gender"].count()

other_purchase = purchase_df.loc[purchase_df["Gender"] == "Other / Non-Disclosed", :]
other_purch = other_purchase["Gender"].count()

male_avg_price = round(male_purchase["Price"].mean(),2)
female_avg_price = round(female_purchase["Price"].mean(),2)
other_avg_price = round(other_purchase["Price"].mean(),2)

male_total_purchase = male_purchase["Price"].sum()
female_total_purchase = female_purchase["Price"].sum()
other_total_purchase = other_purchase["Price"].sum()

normalized_male_total = round(male_total_purchase / total_purchase,2)
normalized_female_total = round(female_total_purchase / total_purchase,2)
normalized_other_total = round(other_total_purchase / total_purchase,2)

purchasing_analysis_total = pd.DataFrame({
    "Gender": ["Male", "Female", "Other / Non-Disclosed"],
    "Purchase Count": [male_purch, female_purch, other_purch],
    "Average Purchase Price": [male_avg_price, female_avg_price, other_avg_price],
    "Total Purchase Value": [male_total_purchase, female_total_purchase, other_total_purchase],
    "Normalized Totals": [normalized_male_total, normalized_female_total, normalized_other_total]}, 
    columns=['Gender',
             "Purchase Count",
             "Average Purchase Price",
             "Total Purchase Value",
              "Normalized Totals"])
purchasing_analysis_total["Average Purchase Price"] = purchasing_analysis_total["Average Purchase Price"].map("${:.2f}".format)
purchasing_analysis_total["Total Purchase Value"] = purchasing_analysis_total["Total Purchase Value"].map("${:.2f}".format)
purchasing_analysis_total["Normalized Totals"] = purchasing_analysis_total["Normalized Totals"].map("${:.2f}".format)
purchasing_analysis_total
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Gender</th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Male</td>
      <td>64</td>
      <td>$2.88</td>
      <td>$184.60</td>
      <td>$2.37</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Female</td>
      <td>13</td>
      <td>$3.18</td>
      <td>$41.38</td>
      <td>$0.53</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Other / Non-Disclosed</td>
      <td>1</td>
      <td>$2.12</td>
      <td>$2.12</td>
      <td>$0.03</td>
    </tr>
  </tbody>
</table>
</div>



AGE DEMOGRAPHICS


```python
bins = [0, 10, 14, 19, 24, 29, 34, 39, 45]
group_names = ["<10", '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40+']

players_df["Age Bracket"] = pd.cut(players_df["Age"], bins, labels=group_names)

age_bracket_total = players_df["Age Bracket"].value_counts()
age_bracket_percent = round(age_bracket_total / total_pop *100,2)
age_demographics = pd.DataFrame({"Percent of Players": age_bracket_percent, "Total Count": age_bracket_total})
age_demographics.sort_index()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Percent of Players</th>
      <th>Total Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>5.33</td>
      <td>62</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>3.96</td>
      <td>46</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>17.54</td>
      <td>204</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>41.79</td>
      <td>486</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>16.25</td>
      <td>189</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>8.17</td>
      <td>95</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>5.16</td>
      <td>60</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>1.81</td>
      <td>21</td>
    </tr>
  </tbody>
</table>
</div>



PURCHASING ANALYSIS (AGE)


```python
purchase_df["Age Bracket"] = pd.cut(purchase_df["Age"], bins, labels=group_names)

age_purch_count = purchase_df["Age Bracket"].value_counts()
age_total_purch = purchase_df.groupby(["Age Bracket"]).sum()["Price"]
age_purch_avg = round(purchase_df.groupby(["Age Bracket"]).mean()["Price"],2)
age_normalized = round(age_total_purch / total_purchase,2)

purchasing_analysis_age = pd.DataFrame({"Purchase Count": age_purch_count,
                                       "Average Purchase Price": age_purch_avg,
                                       "Total Purchase Value": age_total_purch,
                                       "Normalized Totals": age_normalized}, columns=["Purchase Count",
                                                                                      "Average Purchase Price",
                                                                                      "Total Purchase Value",
                                                                                      "Normalized Totals"])

purchasing_analysis_age["Average Purchase Price"] = purchasing_analysis_age["Average Purchase Price"].map("${:.2f}".format)
purchasing_analysis_age["Total Purchase Value"] = purchasing_analysis_age["Total Purchase Value"].map("${:.2f}".format)
purchasing_analysis_age["Normalized Totals"] = purchasing_analysis_age["Normalized Totals"].map("${:.2f}".format)
purchasing_analysis_age.index=["<10", '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40+']
purchasing_analysis_age
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>3</td>
      <td>$2.99</td>
      <td>$8.96</td>
      <td>$0.11</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>11</td>
      <td>$2.76</td>
      <td>$30.41</td>
      <td>$0.39</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>36</td>
      <td>$3.02</td>
      <td>$108.89</td>
      <td>$1.40</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>9</td>
      <td>$2.90</td>
      <td>$26.11</td>
      <td>$0.33</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>7</td>
      <td>$1.98</td>
      <td>$13.89</td>
      <td>$0.18</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>6</td>
      <td>$3.56</td>
      <td>$21.37</td>
      <td>$0.27</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>1</td>
      <td>$4.65</td>
      <td>$4.65</td>
      <td>$0.06</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>5</td>
      <td>$2.76</td>
      <td>$13.82</td>
      <td>$0.18</td>
    </tr>
  </tbody>
</table>
</div>



TOP SPENDERS


```python
ts_purchase_count = purchase_df["SN"].value_counts()
ts_purchase_amt = purchase_df.groupby(["SN"]).sum()["Price"]
ts_avg_purch_price = purchase_df.groupby(["SN"]).mean()["Price"]

top_spenders_df = pd.DataFrame({"Purchase Count": ts_purchase_count,
                               "Average Purchase Price": ts_avg_purch_price,
                               "Total Purchase Value": ts_purchase_amt}, columns=["Purchase Count",
                                                                                 "Average Purchase Price",
                                                                                 "Total Purchase Value"])

top_spenders_df["Average Purchase Price"] = top_spenders_df["Average Purchase Price"].map("${:.2f}".format)
top_spenders_df["Total Purchase Value"] = top_spenders_df["Total Purchase Value"].map("${:.2f}".format)
top_spenders_df.sort_values(by="Total Purchase Value", ascending = False).head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Sundaky74</th>
      <td>2</td>
      <td>$3.71</td>
      <td>$7.41</td>
    </tr>
    <tr>
      <th>Aidaira26</th>
      <td>2</td>
      <td>$2.56</td>
      <td>$5.13</td>
    </tr>
    <tr>
      <th>Eusty71</th>
      <td>1</td>
      <td>$4.81</td>
      <td>$4.81</td>
    </tr>
    <tr>
      <th>Chanirra64</th>
      <td>1</td>
      <td>$4.78</td>
      <td>$4.78</td>
    </tr>
    <tr>
      <th>Alarap40</th>
      <td>1</td>
      <td>$4.71</td>
      <td>$4.71</td>
    </tr>
  </tbody>
</table>
</div>



MOST POPULAR ITEMS


```python
item_data = purchase_df.loc[:,["Item ID", "Item Name", "Price"]]

item_purchase_count = item_data.groupby(["Item ID", "Item Name"]).count()["Price"]
item_price = item_data.groupby(["Item ID", "Item Name"]).mean()["Price"]
item_purchase_value = item_data.groupby(["Item ID", "Item Name"]).sum()["Price"]

most_popular_items = pd.DataFrame({"Purchase Count": item_purchase_count, 
                                  "Item Price": item_price,
                                  "Total Purchase Value": item_purchase_value}, columns =["Purchase Count",
                                                                                        "Item Price",
                                                                                         "Total Purchase Value"])
most_popular_items["Item Price"] = most_popular_items["Item Price"].map("${:,.2f}".format)
most_popular_items["Purchase Count"] = most_popular_items["Purchase Count"].map("{:,}".format)
most_popular_items["Total Purchase Value"] = most_popular_items["Total Purchase Value"].map("${:,.2f}".format)
most_popular_items = most_popular_items.loc[:,["Purchase Count", "Item Price", "Total Purchase Value"]]
most_popular_items.sort_values("Purchase Count", ascending=False).head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>94</th>
      <th>Mourning Blade</th>
      <td>3</td>
      <td>$3.64</td>
      <td>$10.92</td>
    </tr>
    <tr>
      <th>90</th>
      <th>Betrayer</th>
      <td>2</td>
      <td>$4.12</td>
      <td>$8.24</td>
    </tr>
    <tr>
      <th>111</th>
      <th>Misery's End</th>
      <td>2</td>
      <td>$1.79</td>
      <td>$3.58</td>
    </tr>
    <tr>
      <th>64</th>
      <th>Fusion Pummel</th>
      <td>2</td>
      <td>$2.42</td>
      <td>$4.84</td>
    </tr>
    <tr>
      <th>154</th>
      <th>Feral Katana</th>
      <td>2</td>
      <td>$4.11</td>
      <td>$8.22</td>
    </tr>
  </tbody>
</table>
</div>



MOST PROFITABLE ITEMS


```python
most_popular_items.sort_values("Total Purchase Value", ascending=False).head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>117</th>
      <th>Heartstriker, Legacy of the Light</th>
      <td>2</td>
      <td>$4.71</td>
      <td>$9.42</td>
    </tr>
    <tr>
      <th>93</th>
      <th>Apocalyptic Battlescythe</th>
      <td>2</td>
      <td>$4.49</td>
      <td>$8.98</td>
    </tr>
    <tr>
      <th>90</th>
      <th>Betrayer</th>
      <td>2</td>
      <td>$4.12</td>
      <td>$8.24</td>
    </tr>
    <tr>
      <th>154</th>
      <th>Feral Katana</th>
      <td>2</td>
      <td>$4.11</td>
      <td>$8.22</td>
    </tr>
    <tr>
      <th>180</th>
      <th>Stormcaller</th>
      <td>2</td>
      <td>$2.77</td>
      <td>$5.54</td>
    </tr>
  </tbody>
</table>
</div>




```python
#You must submit a link to your Jupyter Notebook with the viewable Data Frames.
#You must include an exported markdown version of your Notebook called  README.md in your GitHub repository.
Heroes Of Pymoli Data Analysis:
    
1. Even though males make up a majorityof the player population (82%) and had a higher total spending, 
the average purhcase by female players was $0.30 higher than the average male player purchase.

2. Players between the ages of 15 and 19 had the highest total purchases at $108.89, but players between 35 and 39 had
the highest average purchase price at $4.65.

3. Even though they make up over 40% of the games player population, 20 to 24 year olds rank 5th in average purchase price,
telling us that most of them are not buying larger ticket items. 
```
