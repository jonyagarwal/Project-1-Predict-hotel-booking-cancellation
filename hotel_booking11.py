{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "0c5ae812",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c17044e7",
   "metadata": {},
   "outputs": [],
   "source": [
    "df=pd.read_csv(\"hotel_bookings.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "333abc02",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>hotel</th>\n",
       "      <th>is_canceled</th>\n",
       "      <th>lead_time</th>\n",
       "      <th>arrival_date_year</th>\n",
       "      <th>arrival_date_month</th>\n",
       "      <th>arrival_date_week_number</th>\n",
       "      <th>arrival_date_day_of_month</th>\n",
       "      <th>stays_in_weekend_nights</th>\n",
       "      <th>stays_in_week_nights</th>\n",
       "      <th>adults</th>\n",
       "      <th>...</th>\n",
       "      <th>deposit_type</th>\n",
       "      <th>agent</th>\n",
       "      <th>company</th>\n",
       "      <th>days_in_waiting_list</th>\n",
       "      <th>customer_type</th>\n",
       "      <th>adr</th>\n",
       "      <th>required_car_parking_spaces</th>\n",
       "      <th>total_of_special_requests</th>\n",
       "      <th>reservation_status</th>\n",
       "      <th>reservation_status_date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>0</td>\n",
       "      <td>342</td>\n",
       "      <td>2015</td>\n",
       "      <td>July</td>\n",
       "      <td>27</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>...</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "      <td>Transient</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Check-Out</td>\n",
       "      <td>7/1/2015</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>0</td>\n",
       "      <td>737</td>\n",
       "      <td>2015</td>\n",
       "      <td>July</td>\n",
       "      <td>27</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>...</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "      <td>Transient</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Check-Out</td>\n",
       "      <td>7/1/2015</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>0</td>\n",
       "      <td>7</td>\n",
       "      <td>2015</td>\n",
       "      <td>July</td>\n",
       "      <td>27</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>...</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "      <td>Transient</td>\n",
       "      <td>75.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Check-Out</td>\n",
       "      <td>7/2/2015</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>0</td>\n",
       "      <td>13</td>\n",
       "      <td>2015</td>\n",
       "      <td>July</td>\n",
       "      <td>27</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>...</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>304.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "      <td>Transient</td>\n",
       "      <td>75.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Check-Out</td>\n",
       "      <td>7/2/2015</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>0</td>\n",
       "      <td>14</td>\n",
       "      <td>2015</td>\n",
       "      <td>July</td>\n",
       "      <td>27</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>...</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>240.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "      <td>Transient</td>\n",
       "      <td>98.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>Check-Out</td>\n",
       "      <td>7/3/2015</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 32 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "          hotel  is_canceled  lead_time  arrival_date_year arrival_date_month  \\\n",
       "0  Resort Hotel            0        342               2015               July   \n",
       "1  Resort Hotel            0        737               2015               July   \n",
       "2  Resort Hotel            0          7               2015               July   \n",
       "3  Resort Hotel            0         13               2015               July   \n",
       "4  Resort Hotel            0         14               2015               July   \n",
       "\n",
       "   arrival_date_week_number  arrival_date_day_of_month  \\\n",
       "0                        27                          1   \n",
       "1                        27                          1   \n",
       "2                        27                          1   \n",
       "3                        27                          1   \n",
       "4                        27                          1   \n",
       "\n",
       "   stays_in_weekend_nights  stays_in_week_nights  adults  ...  deposit_type  \\\n",
       "0                        0                     0       2  ...    No Deposit   \n",
       "1                        0                     0       2  ...    No Deposit   \n",
       "2                        0                     1       1  ...    No Deposit   \n",
       "3                        0                     1       1  ...    No Deposit   \n",
       "4                        0                     2       2  ...    No Deposit   \n",
       "\n",
       "   agent company days_in_waiting_list customer_type   adr  \\\n",
       "0    NaN     NaN                    0     Transient   0.0   \n",
       "1    NaN     NaN                    0     Transient   0.0   \n",
       "2    NaN     NaN                    0     Transient  75.0   \n",
       "3  304.0     NaN                    0     Transient  75.0   \n",
       "4  240.0     NaN                    0     Transient  98.0   \n",
       "\n",
       "   required_car_parking_spaces  total_of_special_requests  reservation_status  \\\n",
       "0                            0                          0           Check-Out   \n",
       "1                            0                          0           Check-Out   \n",
       "2                            0                          0           Check-Out   \n",
       "3                            0                          0           Check-Out   \n",
       "4                            0                          1           Check-Out   \n",
       "\n",
       "  reservation_status_date  \n",
       "0                7/1/2015  \n",
       "1                7/1/2015  \n",
       "2                7/2/2015  \n",
       "3                7/2/2015  \n",
       "4                7/3/2015  \n",
       "\n",
       "[5 rows x 32 columns]"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "2671d1ad",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(119390, 32)"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "7e609349",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "hotel                                  0\n",
       "is_canceled                            0\n",
       "lead_time                              0\n",
       "arrival_date_year                      0\n",
       "arrival_date_month                     0\n",
       "arrival_date_week_number               0\n",
       "arrival_date_day_of_month              0\n",
       "stays_in_weekend_nights                0\n",
       "stays_in_week_nights                   0\n",
       "adults                                 0\n",
       "children                               4\n",
       "babies                                 0\n",
       "meal                                   0\n",
       "country                              488\n",
       "market_segment                         0\n",
       "distribution_channel                   0\n",
       "is_repeated_guest                      0\n",
       "previous_cancellations                 0\n",
       "previous_bookings_not_canceled         0\n",
       "reserved_room_type                     0\n",
       "assigned_room_type                     0\n",
       "booking_changes                        0\n",
       "deposit_type                           0\n",
       "agent                              16340\n",
       "company                           112593\n",
       "days_in_waiting_list                   0\n",
       "customer_type                          0\n",
       "adr                                    0\n",
       "required_car_parking_spaces            0\n",
       "total_of_special_requests              0\n",
       "reservation_status                     0\n",
       "reservation_status_date                0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isna().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "df3e2b65",
   "metadata": {},
   "outputs": [],
   "source": [
    "def data_clean(df):\n",
    "    df.fillna(0,inplace=True)\n",
    "    print(df.isnull().sum())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "49b88c03",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hotel                             0\n",
      "is_canceled                       0\n",
      "lead_time                         0\n",
      "arrival_date_year                 0\n",
      "arrival_date_month                0\n",
      "arrival_date_week_number          0\n",
      "arrival_date_day_of_month         0\n",
      "stays_in_weekend_nights           0\n",
      "stays_in_week_nights              0\n",
      "adults                            0\n",
      "children                          0\n",
      "babies                            0\n",
      "meal                              0\n",
      "country                           0\n",
      "market_segment                    0\n",
      "distribution_channel              0\n",
      "is_repeated_guest                 0\n",
      "previous_cancellations            0\n",
      "previous_bookings_not_canceled    0\n",
      "reserved_room_type                0\n",
      "assigned_room_type                0\n",
      "booking_changes                   0\n",
      "deposit_type                      0\n",
      "agent                             0\n",
      "company                           0\n",
      "days_in_waiting_list              0\n",
      "customer_type                     0\n",
      "adr                               0\n",
      "required_car_parking_spaces       0\n",
      "total_of_special_requests         0\n",
      "reservation_status                0\n",
      "reservation_status_date           0\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "data_clean(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "ee1ac73d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['hotel', 'is_canceled', 'lead_time', 'arrival_date_year',\n",
       "       'arrival_date_month', 'arrival_date_week_number',\n",
       "       'arrival_date_day_of_month', 'stays_in_weekend_nights',\n",
       "       'stays_in_week_nights', 'adults', 'children', 'babies', 'meal',\n",
       "       'country', 'market_segment', 'distribution_channel',\n",
       "       'is_repeated_guest', 'previous_cancellations',\n",
       "       'previous_bookings_not_canceled', 'reserved_room_type',\n",
       "       'assigned_room_type', 'booking_changes', 'deposit_type', 'agent',\n",
       "       'company', 'days_in_waiting_list', 'customer_type', 'adr',\n",
       "       'required_car_parking_spaces', 'total_of_special_requests',\n",
       "       'reservation_status', 'reservation_status_date'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "b7702c22",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "adults has unique values as [ 2  1  3  4 40 26 50 27 55  0 20  6  5 10]\n",
      "children has unique values as [ 0.  1.  2. 10.  3.]\n",
      "babies has unique values as [ 0  1  2 10  9]\n"
     ]
    }
   ],
   "source": [
    "list=['adults', 'children', 'babies']\n",
    "for i in list:\n",
    "    print('{} has unique values as {}'.format(i,df[i].unique()))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "9fc58af2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>hotel</th>\n",
       "      <th>is_canceled</th>\n",
       "      <th>lead_time</th>\n",
       "      <th>arrival_date_year</th>\n",
       "      <th>arrival_date_month</th>\n",
       "      <th>arrival_date_week_number</th>\n",
       "      <th>arrival_date_day_of_month</th>\n",
       "      <th>stays_in_weekend_nights</th>\n",
       "      <th>stays_in_week_nights</th>\n",
       "      <th>adults</th>\n",
       "      <th>...</th>\n",
       "      <th>deposit_type</th>\n",
       "      <th>agent</th>\n",
       "      <th>company</th>\n",
       "      <th>days_in_waiting_list</th>\n",
       "      <th>customer_type</th>\n",
       "      <th>adr</th>\n",
       "      <th>required_car_parking_spaces</th>\n",
       "      <th>total_of_special_requests</th>\n",
       "      <th>reservation_status</th>\n",
       "      <th>reservation_status_date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2224</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>2015</td>\n",
       "      <td>October</td>\n",
       "      <td>41</td>\n",
       "      <td>6</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>0.0</td>\n",
       "      <td>174.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Transient-Party</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Check-Out</td>\n",
       "      <td>10/6/2015</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2409</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>2015</td>\n",
       "      <td>October</td>\n",
       "      <td>42</td>\n",
       "      <td>12</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>0.0</td>\n",
       "      <td>174.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Transient</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Check-Out</td>\n",
       "      <td>10/12/2015</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3181</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>0</td>\n",
       "      <td>36</td>\n",
       "      <td>2015</td>\n",
       "      <td>November</td>\n",
       "      <td>47</td>\n",
       "      <td>20</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>38.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Transient-Party</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Check-Out</td>\n",
       "      <td>11/23/2015</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3684</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>0</td>\n",
       "      <td>165</td>\n",
       "      <td>2015</td>\n",
       "      <td>December</td>\n",
       "      <td>53</td>\n",
       "      <td>30</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>308.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>122</td>\n",
       "      <td>Transient-Party</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Check-Out</td>\n",
       "      <td>1/4/2016</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3708</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>0</td>\n",
       "      <td>165</td>\n",
       "      <td>2015</td>\n",
       "      <td>December</td>\n",
       "      <td>53</td>\n",
       "      <td>30</td>\n",
       "      <td>2</td>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>308.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>122</td>\n",
       "      <td>Transient-Party</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Check-Out</td>\n",
       "      <td>1/5/2016</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>115029</th>\n",
       "      <td>City Hotel</td>\n",
       "      <td>0</td>\n",
       "      <td>107</td>\n",
       "      <td>2017</td>\n",
       "      <td>June</td>\n",
       "      <td>26</td>\n",
       "      <td>27</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>7.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Transient</td>\n",
       "      <td>100.80</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Check-Out</td>\n",
       "      <td>6/30/2017</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>115091</th>\n",
       "      <td>City Hotel</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>2017</td>\n",
       "      <td>June</td>\n",
       "      <td>26</td>\n",
       "      <td>30</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Transient</td>\n",
       "      <td>0.00</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Check-Out</td>\n",
       "      <td>7/1/2017</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>116251</th>\n",
       "      <td>City Hotel</td>\n",
       "      <td>0</td>\n",
       "      <td>44</td>\n",
       "      <td>2017</td>\n",
       "      <td>July</td>\n",
       "      <td>28</td>\n",
       "      <td>15</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>425.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Transient</td>\n",
       "      <td>73.80</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Check-Out</td>\n",
       "      <td>7/17/2017</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>116534</th>\n",
       "      <td>City Hotel</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>2017</td>\n",
       "      <td>July</td>\n",
       "      <td>28</td>\n",
       "      <td>15</td>\n",
       "      <td>2</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>9.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Transient-Party</td>\n",
       "      <td>22.86</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>Check-Out</td>\n",
       "      <td>7/22/2017</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>117087</th>\n",
       "      <td>City Hotel</td>\n",
       "      <td>0</td>\n",
       "      <td>170</td>\n",
       "      <td>2017</td>\n",
       "      <td>July</td>\n",
       "      <td>30</td>\n",
       "      <td>27</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>52.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Transient</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Check-Out</td>\n",
       "      <td>7/29/2017</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>180 rows × 32 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "               hotel  is_canceled  lead_time  arrival_date_year  \\\n",
       "2224    Resort Hotel            0          1               2015   \n",
       "2409    Resort Hotel            0          0               2015   \n",
       "3181    Resort Hotel            0         36               2015   \n",
       "3684    Resort Hotel            0        165               2015   \n",
       "3708    Resort Hotel            0        165               2015   \n",
       "...              ...          ...        ...                ...   \n",
       "115029    City Hotel            0        107               2017   \n",
       "115091    City Hotel            0          1               2017   \n",
       "116251    City Hotel            0         44               2017   \n",
       "116534    City Hotel            0          2               2017   \n",
       "117087    City Hotel            0        170               2017   \n",
       "\n",
       "       arrival_date_month  arrival_date_week_number  \\\n",
       "2224              October                        41   \n",
       "2409              October                        42   \n",
       "3181             November                        47   \n",
       "3684             December                        53   \n",
       "3708             December                        53   \n",
       "...                   ...                       ...   \n",
       "115029               June                        26   \n",
       "115091               June                        26   \n",
       "116251               July                        28   \n",
       "116534               July                        28   \n",
       "117087               July                        30   \n",
       "\n",
       "        arrival_date_day_of_month  stays_in_weekend_nights  \\\n",
       "2224                            6                        0   \n",
       "2409                           12                        0   \n",
       "3181                           20                        1   \n",
       "3684                           30                        1   \n",
       "3708                           30                        2   \n",
       "...                           ...                      ...   \n",
       "115029                         27                        0   \n",
       "115091                         30                        0   \n",
       "116251                         15                        1   \n",
       "116534                         15                        2   \n",
       "117087                         27                        0   \n",
       "\n",
       "        stays_in_week_nights  adults  ...  deposit_type  agent company  \\\n",
       "2224                       3       0  ...    No Deposit    0.0   174.0   \n",
       "2409                       0       0  ...    No Deposit    0.0   174.0   \n",
       "3181                       2       0  ...    No Deposit   38.0     0.0   \n",
       "3684                       4       0  ...    No Deposit  308.0     0.0   \n",
       "3708                       4       0  ...    No Deposit  308.0     0.0   \n",
       "...                      ...     ...  ...           ...    ...     ...   \n",
       "115029                     3       0  ...    No Deposit    7.0     0.0   \n",
       "115091                     1       0  ...    No Deposit    0.0     0.0   \n",
       "116251                     1       0  ...    No Deposit  425.0     0.0   \n",
       "116534                     5       0  ...    No Deposit    9.0     0.0   \n",
       "117087                     2       0  ...    No Deposit   52.0     0.0   \n",
       "\n",
       "       days_in_waiting_list    customer_type     adr  \\\n",
       "2224                      0  Transient-Party    0.00   \n",
       "2409                      0        Transient    0.00   \n",
       "3181                      0  Transient-Party    0.00   \n",
       "3684                    122  Transient-Party    0.00   \n",
       "3708                    122  Transient-Party    0.00   \n",
       "...                     ...              ...     ...   \n",
       "115029                    0        Transient  100.80   \n",
       "115091                    0        Transient    0.00   \n",
       "116251                    0        Transient   73.80   \n",
       "116534                    0  Transient-Party   22.86   \n",
       "117087                    0        Transient    0.00   \n",
       "\n",
       "        required_car_parking_spaces  total_of_special_requests  \\\n",
       "2224                              0                          0   \n",
       "2409                              0                          0   \n",
       "3181                              0                          0   \n",
       "3684                              0                          0   \n",
       "3708                              0                          0   \n",
       "...                             ...                        ...   \n",
       "115029                            0                          0   \n",
       "115091                            1                          1   \n",
       "116251                            0                          0   \n",
       "116534                            0                          1   \n",
       "117087                            0                          0   \n",
       "\n",
       "        reservation_status reservation_status_date  \n",
       "2224             Check-Out               10/6/2015  \n",
       "2409             Check-Out              10/12/2015  \n",
       "3181             Check-Out              11/23/2015  \n",
       "3684             Check-Out                1/4/2016  \n",
       "3708             Check-Out                1/5/2016  \n",
       "...                    ...                     ...  \n",
       "115029           Check-Out               6/30/2017  \n",
       "115091           Check-Out                7/1/2017  \n",
       "116251           Check-Out               7/17/2017  \n",
       "116534           Check-Out               7/22/2017  \n",
       "117087           Check-Out               7/29/2017  \n",
       "\n",
       "[180 rows x 32 columns]"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "filter=(df['children']==0)&(df['adults']==0)&(df['babies']==0)\n",
    "df[filter]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "34f4dcf3",
   "metadata": {},
   "outputs": [],
   "source": [
    "pd.set_option('display.max_columns',32)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "bd2db7b0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>hotel</th>\n",
       "      <th>is_canceled</th>\n",
       "      <th>lead_time</th>\n",
       "      <th>arrival_date_year</th>\n",
       "      <th>arrival_date_month</th>\n",
       "      <th>arrival_date_week_number</th>\n",
       "      <th>arrival_date_day_of_month</th>\n",
       "      <th>stays_in_weekend_nights</th>\n",
       "      <th>stays_in_week_nights</th>\n",
       "      <th>adults</th>\n",
       "      <th>children</th>\n",
       "      <th>babies</th>\n",
       "      <th>meal</th>\n",
       "      <th>country</th>\n",
       "      <th>market_segment</th>\n",
       "      <th>distribution_channel</th>\n",
       "      <th>is_repeated_guest</th>\n",
       "      <th>previous_cancellations</th>\n",
       "      <th>previous_bookings_not_canceled</th>\n",
       "      <th>reserved_room_type</th>\n",
       "      <th>assigned_room_type</th>\n",
       "      <th>booking_changes</th>\n",
       "      <th>deposit_type</th>\n",
       "      <th>agent</th>\n",
       "      <th>company</th>\n",
       "      <th>days_in_waiting_list</th>\n",
       "      <th>customer_type</th>\n",
       "      <th>adr</th>\n",
       "      <th>required_car_parking_spaces</th>\n",
       "      <th>total_of_special_requests</th>\n",
       "      <th>reservation_status</th>\n",
       "      <th>reservation_status_date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2224</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>2015</td>\n",
       "      <td>October</td>\n",
       "      <td>41</td>\n",
       "      <td>6</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>SC</td>\n",
       "      <td>PRT</td>\n",
       "      <td>Corporate</td>\n",
       "      <td>Corporate</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>A</td>\n",
       "      <td>I</td>\n",
       "      <td>1</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>0.0</td>\n",
       "      <td>174.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Transient-Party</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Check-Out</td>\n",
       "      <td>10/6/2015</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2409</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>2015</td>\n",
       "      <td>October</td>\n",
       "      <td>42</td>\n",
       "      <td>12</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>SC</td>\n",
       "      <td>PRT</td>\n",
       "      <td>Corporate</td>\n",
       "      <td>Corporate</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>A</td>\n",
       "      <td>I</td>\n",
       "      <td>0</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>0.0</td>\n",
       "      <td>174.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Transient</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Check-Out</td>\n",
       "      <td>10/12/2015</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3181</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>0</td>\n",
       "      <td>36</td>\n",
       "      <td>2015</td>\n",
       "      <td>November</td>\n",
       "      <td>47</td>\n",
       "      <td>20</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>SC</td>\n",
       "      <td>ESP</td>\n",
       "      <td>Groups</td>\n",
       "      <td>TA/TO</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>A</td>\n",
       "      <td>C</td>\n",
       "      <td>0</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>38.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Transient-Party</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Check-Out</td>\n",
       "      <td>11/23/2015</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3684</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>0</td>\n",
       "      <td>165</td>\n",
       "      <td>2015</td>\n",
       "      <td>December</td>\n",
       "      <td>53</td>\n",
       "      <td>30</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>SC</td>\n",
       "      <td>PRT</td>\n",
       "      <td>Groups</td>\n",
       "      <td>TA/TO</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>A</td>\n",
       "      <td>A</td>\n",
       "      <td>1</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>308.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>122</td>\n",
       "      <td>Transient-Party</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Check-Out</td>\n",
       "      <td>1/4/2016</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3708</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>0</td>\n",
       "      <td>165</td>\n",
       "      <td>2015</td>\n",
       "      <td>December</td>\n",
       "      <td>53</td>\n",
       "      <td>30</td>\n",
       "      <td>2</td>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>SC</td>\n",
       "      <td>PRT</td>\n",
       "      <td>Groups</td>\n",
       "      <td>TA/TO</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>A</td>\n",
       "      <td>C</td>\n",
       "      <td>1</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>308.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>122</td>\n",
       "      <td>Transient-Party</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Check-Out</td>\n",
       "      <td>1/5/2016</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>115029</th>\n",
       "      <td>City Hotel</td>\n",
       "      <td>0</td>\n",
       "      <td>107</td>\n",
       "      <td>2017</td>\n",
       "      <td>June</td>\n",
       "      <td>26</td>\n",
       "      <td>27</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>BB</td>\n",
       "      <td>CHE</td>\n",
       "      <td>Online TA</td>\n",
       "      <td>TA/TO</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>A</td>\n",
       "      <td>A</td>\n",
       "      <td>1</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>7.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Transient</td>\n",
       "      <td>100.80</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Check-Out</td>\n",
       "      <td>6/30/2017</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>115091</th>\n",
       "      <td>City Hotel</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>2017</td>\n",
       "      <td>June</td>\n",
       "      <td>26</td>\n",
       "      <td>30</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>SC</td>\n",
       "      <td>PRT</td>\n",
       "      <td>Complementary</td>\n",
       "      <td>Direct</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>E</td>\n",
       "      <td>K</td>\n",
       "      <td>0</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Transient</td>\n",
       "      <td>0.00</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Check-Out</td>\n",
       "      <td>7/1/2017</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>116251</th>\n",
       "      <td>City Hotel</td>\n",
       "      <td>0</td>\n",
       "      <td>44</td>\n",
       "      <td>2017</td>\n",
       "      <td>July</td>\n",
       "      <td>28</td>\n",
       "      <td>15</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>SC</td>\n",
       "      <td>SWE</td>\n",
       "      <td>Online TA</td>\n",
       "      <td>TA/TO</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>A</td>\n",
       "      <td>K</td>\n",
       "      <td>2</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>425.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Transient</td>\n",
       "      <td>73.80</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Check-Out</td>\n",
       "      <td>7/17/2017</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>116534</th>\n",
       "      <td>City Hotel</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>2017</td>\n",
       "      <td>July</td>\n",
       "      <td>28</td>\n",
       "      <td>15</td>\n",
       "      <td>2</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>SC</td>\n",
       "      <td>RUS</td>\n",
       "      <td>Online TA</td>\n",
       "      <td>TA/TO</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>A</td>\n",
       "      <td>K</td>\n",
       "      <td>1</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>9.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Transient-Party</td>\n",
       "      <td>22.86</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>Check-Out</td>\n",
       "      <td>7/22/2017</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>117087</th>\n",
       "      <td>City Hotel</td>\n",
       "      <td>0</td>\n",
       "      <td>170</td>\n",
       "      <td>2017</td>\n",
       "      <td>July</td>\n",
       "      <td>30</td>\n",
       "      <td>27</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>BB</td>\n",
       "      <td>BRA</td>\n",
       "      <td>Offline TA/TO</td>\n",
       "      <td>TA/TO</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>A</td>\n",
       "      <td>A</td>\n",
       "      <td>0</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>52.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Transient</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Check-Out</td>\n",
       "      <td>7/29/2017</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>180 rows × 32 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "               hotel  is_canceled  lead_time  arrival_date_year  \\\n",
       "2224    Resort Hotel            0          1               2015   \n",
       "2409    Resort Hotel            0          0               2015   \n",
       "3181    Resort Hotel            0         36               2015   \n",
       "3684    Resort Hotel            0        165               2015   \n",
       "3708    Resort Hotel            0        165               2015   \n",
       "...              ...          ...        ...                ...   \n",
       "115029    City Hotel            0        107               2017   \n",
       "115091    City Hotel            0          1               2017   \n",
       "116251    City Hotel            0         44               2017   \n",
       "116534    City Hotel            0          2               2017   \n",
       "117087    City Hotel            0        170               2017   \n",
       "\n",
       "       arrival_date_month  arrival_date_week_number  \\\n",
       "2224              October                        41   \n",
       "2409              October                        42   \n",
       "3181             November                        47   \n",
       "3684             December                        53   \n",
       "3708             December                        53   \n",
       "...                   ...                       ...   \n",
       "115029               June                        26   \n",
       "115091               June                        26   \n",
       "116251               July                        28   \n",
       "116534               July                        28   \n",
       "117087               July                        30   \n",
       "\n",
       "        arrival_date_day_of_month  stays_in_weekend_nights  \\\n",
       "2224                            6                        0   \n",
       "2409                           12                        0   \n",
       "3181                           20                        1   \n",
       "3684                           30                        1   \n",
       "3708                           30                        2   \n",
       "...                           ...                      ...   \n",
       "115029                         27                        0   \n",
       "115091                         30                        0   \n",
       "116251                         15                        1   \n",
       "116534                         15                        2   \n",
       "117087                         27                        0   \n",
       "\n",
       "        stays_in_week_nights  adults  children  babies meal country  \\\n",
       "2224                       3       0       0.0       0   SC     PRT   \n",
       "2409                       0       0       0.0       0   SC     PRT   \n",
       "3181                       2       0       0.0       0   SC     ESP   \n",
       "3684                       4       0       0.0       0   SC     PRT   \n",
       "3708                       4       0       0.0       0   SC     PRT   \n",
       "...                      ...     ...       ...     ...  ...     ...   \n",
       "115029                     3       0       0.0       0   BB     CHE   \n",
       "115091                     1       0       0.0       0   SC     PRT   \n",
       "116251                     1       0       0.0       0   SC     SWE   \n",
       "116534                     5       0       0.0       0   SC     RUS   \n",
       "117087                     2       0       0.0       0   BB     BRA   \n",
       "\n",
       "       market_segment distribution_channel  is_repeated_guest  \\\n",
       "2224        Corporate            Corporate                  0   \n",
       "2409        Corporate            Corporate                  0   \n",
       "3181           Groups                TA/TO                  0   \n",
       "3684           Groups                TA/TO                  0   \n",
       "3708           Groups                TA/TO                  0   \n",
       "...               ...                  ...                ...   \n",
       "115029      Online TA                TA/TO                  0   \n",
       "115091  Complementary               Direct                  0   \n",
       "116251      Online TA                TA/TO                  0   \n",
       "116534      Online TA                TA/TO                  0   \n",
       "117087  Offline TA/TO                TA/TO                  0   \n",
       "\n",
       "        previous_cancellations  previous_bookings_not_canceled  \\\n",
       "2224                         0                               0   \n",
       "2409                         0                               0   \n",
       "3181                         0                               0   \n",
       "3684                         0                               0   \n",
       "3708                         0                               0   \n",
       "...                        ...                             ...   \n",
       "115029                       0                               0   \n",
       "115091                       0                               0   \n",
       "116251                       0                               0   \n",
       "116534                       0                               0   \n",
       "117087                       0                               0   \n",
       "\n",
       "       reserved_room_type assigned_room_type  booking_changes deposit_type  \\\n",
       "2224                    A                  I                1   No Deposit   \n",
       "2409                    A                  I                0   No Deposit   \n",
       "3181                    A                  C                0   No Deposit   \n",
       "3684                    A                  A                1   No Deposit   \n",
       "3708                    A                  C                1   No Deposit   \n",
       "...                   ...                ...              ...          ...   \n",
       "115029                  A                  A                1   No Deposit   \n",
       "115091                  E                  K                0   No Deposit   \n",
       "116251                  A                  K                2   No Deposit   \n",
       "116534                  A                  K                1   No Deposit   \n",
       "117087                  A                  A                0   No Deposit   \n",
       "\n",
       "        agent  company  days_in_waiting_list    customer_type     adr  \\\n",
       "2224      0.0    174.0                     0  Transient-Party    0.00   \n",
       "2409      0.0    174.0                     0        Transient    0.00   \n",
       "3181     38.0      0.0                     0  Transient-Party    0.00   \n",
       "3684    308.0      0.0                   122  Transient-Party    0.00   \n",
       "3708    308.0      0.0                   122  Transient-Party    0.00   \n",
       "...       ...      ...                   ...              ...     ...   \n",
       "115029    7.0      0.0                     0        Transient  100.80   \n",
       "115091    0.0      0.0                     0        Transient    0.00   \n",
       "116251  425.0      0.0                     0        Transient   73.80   \n",
       "116534    9.0      0.0                     0  Transient-Party   22.86   \n",
       "117087   52.0      0.0                     0        Transient    0.00   \n",
       "\n",
       "        required_car_parking_spaces  total_of_special_requests  \\\n",
       "2224                              0                          0   \n",
       "2409                              0                          0   \n",
       "3181                              0                          0   \n",
       "3684                              0                          0   \n",
       "3708                              0                          0   \n",
       "...                             ...                        ...   \n",
       "115029                            0                          0   \n",
       "115091                            1                          1   \n",
       "116251                            0                          0   \n",
       "116534                            0                          1   \n",
       "117087                            0                          0   \n",
       "\n",
       "       reservation_status reservation_status_date  \n",
       "2224            Check-Out               10/6/2015  \n",
       "2409            Check-Out              10/12/2015  \n",
       "3181            Check-Out              11/23/2015  \n",
       "3684            Check-Out                1/4/2016  \n",
       "3708            Check-Out                1/5/2016  \n",
       "...                   ...                     ...  \n",
       "115029          Check-Out               6/30/2017  \n",
       "115091          Check-Out                7/1/2017  \n",
       "116251          Check-Out               7/17/2017  \n",
       "116534          Check-Out               7/22/2017  \n",
       "117087          Check-Out               7/29/2017  \n",
       "\n",
       "[180 rows x 32 columns]"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "filter=(df['children']==0)&(df['adults']==0)&(df['babies']==0)\n",
    "df[filter]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "553d2b41",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>hotel</th>\n",
       "      <th>is_canceled</th>\n",
       "      <th>lead_time</th>\n",
       "      <th>arrival_date_year</th>\n",
       "      <th>arrival_date_month</th>\n",
       "      <th>arrival_date_week_number</th>\n",
       "      <th>arrival_date_day_of_month</th>\n",
       "      <th>stays_in_weekend_nights</th>\n",
       "      <th>stays_in_week_nights</th>\n",
       "      <th>adults</th>\n",
       "      <th>children</th>\n",
       "      <th>babies</th>\n",
       "      <th>meal</th>\n",
       "      <th>country</th>\n",
       "      <th>market_segment</th>\n",
       "      <th>distribution_channel</th>\n",
       "      <th>is_repeated_guest</th>\n",
       "      <th>previous_cancellations</th>\n",
       "      <th>previous_bookings_not_canceled</th>\n",
       "      <th>reserved_room_type</th>\n",
       "      <th>assigned_room_type</th>\n",
       "      <th>booking_changes</th>\n",
       "      <th>deposit_type</th>\n",
       "      <th>agent</th>\n",
       "      <th>company</th>\n",
       "      <th>days_in_waiting_list</th>\n",
       "      <th>customer_type</th>\n",
       "      <th>adr</th>\n",
       "      <th>required_car_parking_spaces</th>\n",
       "      <th>total_of_special_requests</th>\n",
       "      <th>reservation_status</th>\n",
       "      <th>reservation_status_date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>0</td>\n",
       "      <td>342</td>\n",
       "      <td>2015</td>\n",
       "      <td>July</td>\n",
       "      <td>27</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>BB</td>\n",
       "      <td>PRT</td>\n",
       "      <td>Direct</td>\n",
       "      <td>Direct</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>C</td>\n",
       "      <td>C</td>\n",
       "      <td>3</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Transient</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Check-Out</td>\n",
       "      <td>7/1/2015</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>0</td>\n",
       "      <td>737</td>\n",
       "      <td>2015</td>\n",
       "      <td>July</td>\n",
       "      <td>27</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>BB</td>\n",
       "      <td>PRT</td>\n",
       "      <td>Direct</td>\n",
       "      <td>Direct</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>C</td>\n",
       "      <td>C</td>\n",
       "      <td>4</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Transient</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Check-Out</td>\n",
       "      <td>7/1/2015</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>0</td>\n",
       "      <td>7</td>\n",
       "      <td>2015</td>\n",
       "      <td>July</td>\n",
       "      <td>27</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>BB</td>\n",
       "      <td>GBR</td>\n",
       "      <td>Direct</td>\n",
       "      <td>Direct</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>A</td>\n",
       "      <td>C</td>\n",
       "      <td>0</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Transient</td>\n",
       "      <td>75.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Check-Out</td>\n",
       "      <td>7/2/2015</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>0</td>\n",
       "      <td>13</td>\n",
       "      <td>2015</td>\n",
       "      <td>July</td>\n",
       "      <td>27</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>BB</td>\n",
       "      <td>GBR</td>\n",
       "      <td>Corporate</td>\n",
       "      <td>Corporate</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>A</td>\n",
       "      <td>A</td>\n",
       "      <td>0</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>304.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Transient</td>\n",
       "      <td>75.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Check-Out</td>\n",
       "      <td>7/2/2015</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>0</td>\n",
       "      <td>14</td>\n",
       "      <td>2015</td>\n",
       "      <td>July</td>\n",
       "      <td>27</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>BB</td>\n",
       "      <td>GBR</td>\n",
       "      <td>Online TA</td>\n",
       "      <td>TA/TO</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>A</td>\n",
       "      <td>A</td>\n",
       "      <td>0</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>240.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Transient</td>\n",
       "      <td>98.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>Check-Out</td>\n",
       "      <td>7/3/2015</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          hotel  is_canceled  lead_time  arrival_date_year arrival_date_month  \\\n",
       "0  Resort Hotel            0        342               2015               July   \n",
       "1  Resort Hotel            0        737               2015               July   \n",
       "2  Resort Hotel            0          7               2015               July   \n",
       "3  Resort Hotel            0         13               2015               July   \n",
       "4  Resort Hotel            0         14               2015               July   \n",
       "\n",
       "   arrival_date_week_number  arrival_date_day_of_month  \\\n",
       "0                        27                          1   \n",
       "1                        27                          1   \n",
       "2                        27                          1   \n",
       "3                        27                          1   \n",
       "4                        27                          1   \n",
       "\n",
       "   stays_in_weekend_nights  stays_in_week_nights  adults  children  babies  \\\n",
       "0                        0                     0       2       0.0       0   \n",
       "1                        0                     0       2       0.0       0   \n",
       "2                        0                     1       1       0.0       0   \n",
       "3                        0                     1       1       0.0       0   \n",
       "4                        0                     2       2       0.0       0   \n",
       "\n",
       "  meal country market_segment distribution_channel  is_repeated_guest  \\\n",
       "0   BB     PRT         Direct               Direct                  0   \n",
       "1   BB     PRT         Direct               Direct                  0   \n",
       "2   BB     GBR         Direct               Direct                  0   \n",
       "3   BB     GBR      Corporate            Corporate                  0   \n",
       "4   BB     GBR      Online TA                TA/TO                  0   \n",
       "\n",
       "   previous_cancellations  previous_bookings_not_canceled reserved_room_type  \\\n",
       "0                       0                               0                  C   \n",
       "1                       0                               0                  C   \n",
       "2                       0                               0                  A   \n",
       "3                       0                               0                  A   \n",
       "4                       0                               0                  A   \n",
       "\n",
       "  assigned_room_type  booking_changes deposit_type  agent  company  \\\n",
       "0                  C                3   No Deposit    0.0      0.0   \n",
       "1                  C                4   No Deposit    0.0      0.0   \n",
       "2                  C                0   No Deposit    0.0      0.0   \n",
       "3                  A                0   No Deposit  304.0      0.0   \n",
       "4                  A                0   No Deposit  240.0      0.0   \n",
       "\n",
       "   days_in_waiting_list customer_type   adr  required_car_parking_spaces  \\\n",
       "0                     0     Transient   0.0                            0   \n",
       "1                     0     Transient   0.0                            0   \n",
       "2                     0     Transient  75.0                            0   \n",
       "3                     0     Transient  75.0                            0   \n",
       "4                     0     Transient  98.0                            0   \n",
       "\n",
       "   total_of_special_requests reservation_status reservation_status_date  \n",
       "0                          0          Check-Out                7/1/2015  \n",
       "1                          0          Check-Out                7/1/2015  \n",
       "2                          0          Check-Out                7/2/2015  \n",
       "3                          0          Check-Out                7/2/2015  \n",
       "4                          1          Check-Out                7/3/2015  "
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data=df[~filter]\n",
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "f56e2ccd",
   "metadata": {},
   "outputs": [],
   "source": [
    "country_wise_data=data[data['is_canceled']==0]['country'].value_counts().reset_index()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "793ded20",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>country</th>\n",
       "      <th>no. of guests</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>PRT</td>\n",
       "      <td>20977</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>GBR</td>\n",
       "      <td>9668</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>FRA</td>\n",
       "      <td>8468</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>ESP</td>\n",
       "      <td>6383</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>DEU</td>\n",
       "      <td>6067</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>161</th>\n",
       "      <td>PYF</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>162</th>\n",
       "      <td>NCL</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>163</th>\n",
       "      <td>GUY</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>164</th>\n",
       "      <td>BDI</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>165</th>\n",
       "      <td>ATF</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>166 rows × 2 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "    country  no. of guests\n",
       "0       PRT          20977\n",
       "1       GBR           9668\n",
       "2       FRA           8468\n",
       "3       ESP           6383\n",
       "4       DEU           6067\n",
       "..      ...            ...\n",
       "161     PYF              1\n",
       "162     NCL              1\n",
       "163     GUY              1\n",
       "164     BDI              1\n",
       "165     ATF              1\n",
       "\n",
       "[166 rows x 2 columns]"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "country_wise_data.columns=['country','no. of guests']\n",
    "country_wise_data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "f870d6d6",
   "metadata": {},
   "outputs": [],
   "source": [
    "import folium\n",
    "from folium.plugins import HeatMap"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "0a0237d9",
   "metadata": {},
   "outputs": [],
   "source": [
    "basemap=folium.Map()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "cc882150",
   "metadata": {},
   "outputs": [],
   "source": [
    "import plotly.express as px "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "2c2c9d3d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "coloraxis": "coloraxis",
         "geo": "geo",
         "hovertemplate": "<b>%{hovertext}</b><br><br>country=%{location}<br>no. of guests=%{z}<extra></extra>",
         "hovertext": [
          "PRT",
          "GBR",
          "FRA",
          "ESP",
          "DEU",
          "IRL",
          "ITA",
          "BEL",
          "NLD",
          "USA",
          "BRA",
          "CHE",
          "AUT",
          "CN",
          "SWE",
          "POL",
          "CHN",
          "ISR",
          "NOR",
          "0",
          "RUS",
          "FIN",
          "ROU",
          "DNK",
          "AUS",
          "LUX",
          "JPN",
          "ARG",
          "AGO",
          "HUN",
          "MAR",
          "TUR",
          "CZE",
          "IND",
          "SRB",
          "GRC",
          "DZA",
          "KOR",
          "MEX",
          "HRV",
          "LTU",
          "NZL",
          "EST",
          "BGR",
          "IRN",
          "ISL",
          "ZAF",
          "CHL",
          "COL",
          "MOZ",
          "UKR",
          "LVA",
          "SVN",
          "SVK",
          "THA",
          "CYP",
          "TWN",
          "MYS",
          "URY",
          "PER",
          "LBN",
          "SGP",
          "EGY",
          "TUN",
          "ECU",
          "JOR",
          "CRI",
          "BLR",
          "PHL",
          "SAU",
          "IRQ",
          "KAZ",
          "VEN",
          "OMN",
          "NGA",
          "MLT",
          "CPV",
          "IDN",
          "ALB",
          "CMR",
          "KWT",
          "PRI",
          "BOL",
          "BIH",
          "PAN",
          "ARE",
          "MKD",
          "LBY",
          "AZE",
          "CUB",
          "GNB",
          "GEO",
          "GIB",
          "LKA",
          "VNM",
          "ARM",
          "JAM",
          "MUS",
          "DOM",
          "SUR",
          "CAF",
          "PAK",
          "PRY",
          "CIV",
          "QAT",
          "KEN",
          "BRB",
          "GTM",
          "SYR",
          "MCO",
          "MNE",
          "BGD",
          "HKG",
          "SEN",
          "MDV",
          "ATA",
          "TGO",
          "UZB",
          "TZA",
          "COM",
          "LAO",
          "UGA",
          "ABW",
          "LIE",
          "KNA",
          "AND",
          "GAB",
          "MWI",
          "STP",
          "GHA",
          "ZWE",
          "SLV",
          "TMP",
          "ETH",
          "RWA",
          "SLE",
          "MMR",
          "SMR",
          "NAM",
          "MAC",
          "AIA",
          "DMA",
          "LCA",
          "ZMB",
          "NPL",
          "KIR",
          "CYM",
          "FRO",
          "BHS",
          "BWA",
          "MRT",
          "MLI",
          "SYC",
          "SDN",
          "BFA",
          "PLW",
          "ASM",
          "DJI",
          "TJK",
          "BHR",
          "MDG",
          "PYF",
          "NCL",
          "GUY",
          "BDI",
          "ATF"
         ],
         "locations": [
          "PRT",
          "GBR",
          "FRA",
          "ESP",
          "DEU",
          "IRL",
          "ITA",
          "BEL",
          "NLD",
          "USA",
          "BRA",
          "CHE",
          "AUT",
          "CN",
          "SWE",
          "POL",
          "CHN",
          "ISR",
          "NOR",
          0,
          "RUS",
          "FIN",
          "ROU",
          "DNK",
          "AUS",
          "LUX",
          "JPN",
          "ARG",
          "AGO",
          "HUN",
          "MAR",
          "TUR",
          "CZE",
          "IND",
          "SRB",
          "GRC",
          "DZA",
          "KOR",
          "MEX",
          "HRV",
          "LTU",
          "NZL",
          "EST",
          "BGR",
          "IRN",
          "ISL",
          "ZAF",
          "CHL",
          "COL",
          "MOZ",
          "UKR",
          "LVA",
          "SVN",
          "SVK",
          "THA",
          "CYP",
          "TWN",
          "MYS",
          "URY",
          "PER",
          "LBN",
          "SGP",
          "EGY",
          "TUN",
          "ECU",
          "JOR",
          "CRI",
          "BLR",
          "PHL",
          "SAU",
          "IRQ",
          "KAZ",
          "VEN",
          "OMN",
          "NGA",
          "MLT",
          "CPV",
          "IDN",
          "ALB",
          "CMR",
          "KWT",
          "PRI",
          "BOL",
          "BIH",
          "PAN",
          "ARE",
          "MKD",
          "LBY",
          "AZE",
          "CUB",
          "GNB",
          "GEO",
          "GIB",
          "LKA",
          "VNM",
          "ARM",
          "JAM",
          "MUS",
          "DOM",
          "SUR",
          "CAF",
          "PAK",
          "PRY",
          "CIV",
          "QAT",
          "KEN",
          "BRB",
          "GTM",
          "SYR",
          "MCO",
          "MNE",
          "BGD",
          "HKG",
          "SEN",
          "MDV",
          "ATA",
          "TGO",
          "UZB",
          "TZA",
          "COM",
          "LAO",
          "UGA",
          "ABW",
          "LIE",
          "KNA",
          "AND",
          "GAB",
          "MWI",
          "STP",
          "GHA",
          "ZWE",
          "SLV",
          "TMP",
          "ETH",
          "RWA",
          "SLE",
          "MMR",
          "SMR",
          "NAM",
          "MAC",
          "AIA",
          "DMA",
          "LCA",
          "ZMB",
          "NPL",
          "KIR",
          "CYM",
          "FRO",
          "BHS",
          "BWA",
          "MRT",
          "MLI",
          "SYC",
          "SDN",
          "BFA",
          "PLW",
          "ASM",
          "DJI",
          "TJK",
          "BHR",
          "MDG",
          "PYF",
          "NCL",
          "GUY",
          "BDI",
          "ATF"
         ],
         "name": "",
         "type": "choropleth",
         "z": [
          20977,
          9668,
          8468,
          6383,
          6067,
          2542,
          2428,
          1868,
          1716,
          1592,
          1392,
          1298,
          1033,
          1025,
          793,
          703,
          537,
          500,
          426,
          421,
          391,
          377,
          366,
          326,
          319,
          177,
          169,
          160,
          157,
          153,
          150,
          146,
          134,
          116,
          98,
          93,
          82,
          78,
          75,
          75,
          74,
          68,
          65,
          63,
          59,
          53,
          49,
          49,
          48,
          48,
          48,
          46,
          41,
          41,
          41,
          40,
          37,
          25,
          23,
          23,
          22,
          22,
          21,
          20,
          19,
          18,
          18,
          17,
          15,
          15,
          14,
          14,
          14,
          14,
          13,
          13,
          12,
          11,
          10,
          10,
          10,
          10,
          10,
          10,
          9,
          8,
          8,
          8,
          8,
          8,
          8,
          7,
          7,
          7,
          6,
          6,
          6,
          6,
          6,
          5,
          5,
          5,
          4,
          4,
          4,
          4,
          4,
          4,
          3,
          3,
          3,
          3,
          3,
          3,
          3,
          2,
          2,
          2,
          2,
          2,
          2,
          2,
          2,
          2,
          2,
          2,
          2,
          2,
          2,
          2,
          2,
          2,
          2,
          2,
          2,
          1,
          1,
          1,
          1,
          1,
          1,
          1,
          1,
          1,
          1,
          1,
          1,
          1,
          1,
          1,
          1,
          1,
          1,
          1,
          1,
          1,
          1,
          1,
          1,
          1,
          1,
          1,
          1,
          1,
          1,
          1
         ]
        }
       ],
       "layout": {
        "coloraxis": {
         "colorbar": {
          "title": {
           "text": "no. of guests"
          }
         },
         "colorscale": [
          [
           0,
           "#0d0887"
          ],
          [
           0.1111111111111111,
           "#46039f"
          ],
          [
           0.2222222222222222,
           "#7201a8"
          ],
          [
           0.3333333333333333,
           "#9c179e"
          ],
          [
           0.4444444444444444,
           "#bd3786"
          ],
          [
           0.5555555555555556,
           "#d8576b"
          ],
          [
           0.6666666666666666,
           "#ed7953"
          ],
          [
           0.7777777777777778,
           "#fb9f3a"
          ],
          [
           0.8888888888888888,
           "#fdca26"
          ],
          [
           1,
           "#f0f921"
          ]
         ]
        },
        "geo": {
         "center": {},
         "domain": {
          "x": [
           0,
           1
          ],
          "y": [
           0,
           1
          ]
         }
        },
        "legend": {
         "tracegroupgap": 0
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "Home Country of guests"
        }
       }
      },
      "text/html": [
       "<div>                            <div id=\"6081e88f-3fbc-4e63-b31f-267a0ec9413c\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"6081e88f-3fbc-4e63-b31f-267a0ec9413c\")) {                    Plotly.newPlot(                        \"6081e88f-3fbc-4e63-b31f-267a0ec9413c\",                        [{\"coloraxis\":\"coloraxis\",\"geo\":\"geo\",\"hovertemplate\":\"<b>%{hovertext}</b><br><br>country=%{location}<br>no. of guests=%{z}<extra></extra>\",\"hovertext\":[\"PRT\",\"GBR\",\"FRA\",\"ESP\",\"DEU\",\"IRL\",\"ITA\",\"BEL\",\"NLD\",\"USA\",\"BRA\",\"CHE\",\"AUT\",\"CN\",\"SWE\",\"POL\",\"CHN\",\"ISR\",\"NOR\",\"0\",\"RUS\",\"FIN\",\"ROU\",\"DNK\",\"AUS\",\"LUX\",\"JPN\",\"ARG\",\"AGO\",\"HUN\",\"MAR\",\"TUR\",\"CZE\",\"IND\",\"SRB\",\"GRC\",\"DZA\",\"KOR\",\"MEX\",\"HRV\",\"LTU\",\"NZL\",\"EST\",\"BGR\",\"IRN\",\"ISL\",\"ZAF\",\"CHL\",\"COL\",\"MOZ\",\"UKR\",\"LVA\",\"SVN\",\"SVK\",\"THA\",\"CYP\",\"TWN\",\"MYS\",\"URY\",\"PER\",\"LBN\",\"SGP\",\"EGY\",\"TUN\",\"ECU\",\"JOR\",\"CRI\",\"BLR\",\"PHL\",\"SAU\",\"IRQ\",\"KAZ\",\"VEN\",\"OMN\",\"NGA\",\"MLT\",\"CPV\",\"IDN\",\"ALB\",\"CMR\",\"KWT\",\"PRI\",\"BOL\",\"BIH\",\"PAN\",\"ARE\",\"MKD\",\"LBY\",\"AZE\",\"CUB\",\"GNB\",\"GEO\",\"GIB\",\"LKA\",\"VNM\",\"ARM\",\"JAM\",\"MUS\",\"DOM\",\"SUR\",\"CAF\",\"PAK\",\"PRY\",\"CIV\",\"QAT\",\"KEN\",\"BRB\",\"GTM\",\"SYR\",\"MCO\",\"MNE\",\"BGD\",\"HKG\",\"SEN\",\"MDV\",\"ATA\",\"TGO\",\"UZB\",\"TZA\",\"COM\",\"LAO\",\"UGA\",\"ABW\",\"LIE\",\"KNA\",\"AND\",\"GAB\",\"MWI\",\"STP\",\"GHA\",\"ZWE\",\"SLV\",\"TMP\",\"ETH\",\"RWA\",\"SLE\",\"MMR\",\"SMR\",\"NAM\",\"MAC\",\"AIA\",\"DMA\",\"LCA\",\"ZMB\",\"NPL\",\"KIR\",\"CYM\",\"FRO\",\"BHS\",\"BWA\",\"MRT\",\"MLI\",\"SYC\",\"SDN\",\"BFA\",\"PLW\",\"ASM\",\"DJI\",\"TJK\",\"BHR\",\"MDG\",\"PYF\",\"NCL\",\"GUY\",\"BDI\",\"ATF\"],\"locations\":[\"PRT\",\"GBR\",\"FRA\",\"ESP\",\"DEU\",\"IRL\",\"ITA\",\"BEL\",\"NLD\",\"USA\",\"BRA\",\"CHE\",\"AUT\",\"CN\",\"SWE\",\"POL\",\"CHN\",\"ISR\",\"NOR\",0,\"RUS\",\"FIN\",\"ROU\",\"DNK\",\"AUS\",\"LUX\",\"JPN\",\"ARG\",\"AGO\",\"HUN\",\"MAR\",\"TUR\",\"CZE\",\"IND\",\"SRB\",\"GRC\",\"DZA\",\"KOR\",\"MEX\",\"HRV\",\"LTU\",\"NZL\",\"EST\",\"BGR\",\"IRN\",\"ISL\",\"ZAF\",\"CHL\",\"COL\",\"MOZ\",\"UKR\",\"LVA\",\"SVN\",\"SVK\",\"THA\",\"CYP\",\"TWN\",\"MYS\",\"URY\",\"PER\",\"LBN\",\"SGP\",\"EGY\",\"TUN\",\"ECU\",\"JOR\",\"CRI\",\"BLR\",\"PHL\",\"SAU\",\"IRQ\",\"KAZ\",\"VEN\",\"OMN\",\"NGA\",\"MLT\",\"CPV\",\"IDN\",\"ALB\",\"CMR\",\"KWT\",\"PRI\",\"BOL\",\"BIH\",\"PAN\",\"ARE\",\"MKD\",\"LBY\",\"AZE\",\"CUB\",\"GNB\",\"GEO\",\"GIB\",\"LKA\",\"VNM\",\"ARM\",\"JAM\",\"MUS\",\"DOM\",\"SUR\",\"CAF\",\"PAK\",\"PRY\",\"CIV\",\"QAT\",\"KEN\",\"BRB\",\"GTM\",\"SYR\",\"MCO\",\"MNE\",\"BGD\",\"HKG\",\"SEN\",\"MDV\",\"ATA\",\"TGO\",\"UZB\",\"TZA\",\"COM\",\"LAO\",\"UGA\",\"ABW\",\"LIE\",\"KNA\",\"AND\",\"GAB\",\"MWI\",\"STP\",\"GHA\",\"ZWE\",\"SLV\",\"TMP\",\"ETH\",\"RWA\",\"SLE\",\"MMR\",\"SMR\",\"NAM\",\"MAC\",\"AIA\",\"DMA\",\"LCA\",\"ZMB\",\"NPL\",\"KIR\",\"CYM\",\"FRO\",\"BHS\",\"BWA\",\"MRT\",\"MLI\",\"SYC\",\"SDN\",\"BFA\",\"PLW\",\"ASM\",\"DJI\",\"TJK\",\"BHR\",\"MDG\",\"PYF\",\"NCL\",\"GUY\",\"BDI\",\"ATF\"],\"name\":\"\",\"type\":\"choropleth\",\"z\":[20977,9668,8468,6383,6067,2542,2428,1868,1716,1592,1392,1298,1033,1025,793,703,537,500,426,421,391,377,366,326,319,177,169,160,157,153,150,146,134,116,98,93,82,78,75,75,74,68,65,63,59,53,49,49,48,48,48,46,41,41,41,40,37,25,23,23,22,22,21,20,19,18,18,17,15,15,14,14,14,14,13,13,12,11,10,10,10,10,10,10,9,8,8,8,8,8,8,7,7,7,6,6,6,6,6,5,5,5,4,4,4,4,4,4,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]}],                        {\"coloraxis\":{\"colorbar\":{\"title\":{\"text\":\"no. of guests\"}},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]},\"geo\":{\"center\":{},\"domain\":{\"x\":[0.0,1.0],\"y\":[0.0,1.0]}},\"legend\":{\"tracegroupgap\":0},\"template\":{\"data\":{\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"choropleth\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"choropleth\"}],\"contour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"contour\"}],\"contourcarpet\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"contourcarpet\"}],\"heatmap\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmap\"}],\"heatmapgl\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmapgl\"}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"histogram2d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2d\"}],\"histogram2dcontour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2dcontour\"}],\"mesh3d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"mesh3d\"}],\"parcoords\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"parcoords\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}],\"scatter\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter\"}],\"scatter3d\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter3d\"}],\"scattercarpet\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattercarpet\"}],\"scattergeo\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergeo\"}],\"scattergl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergl\"}],\"scattermapbox\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattermapbox\"}],\"scatterpolar\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolar\"}],\"scatterpolargl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolargl\"}],\"scatterternary\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterternary\"}],\"surface\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"surface\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}]},\"layout\":{\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"autotypenumbers\":\"strict\",\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]],\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]},\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"geo\":{\"bgcolor\":\"white\",\"lakecolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"showlakes\":true,\"showland\":true,\"subunitcolor\":\"white\"},\"hoverlabel\":{\"align\":\"left\"},\"hovermode\":\"closest\",\"mapbox\":{\"style\":\"light\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"ternary\":{\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"title\":{\"x\":0.05},\"xaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2},\"yaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2}}},\"title\":{\"text\":\"Home Country of guests\"}},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('6081e88f-3fbc-4e63-b31f-267a0ec9413c');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "map_guest=px.choropleth(country_wise_data,\n",
    "                        locations=country_wise_data['country'],\n",
    "                         color=country_wise_data['no. of guests'],\n",
    "                         hover_name=country_wise_data['country'],\n",
    "                        title='Home Country of guests'\n",
    "                        )\n",
    "map_guest.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "cda37500",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>hotel</th>\n",
       "      <th>is_canceled</th>\n",
       "      <th>lead_time</th>\n",
       "      <th>arrival_date_year</th>\n",
       "      <th>arrival_date_month</th>\n",
       "      <th>arrival_date_week_number</th>\n",
       "      <th>arrival_date_day_of_month</th>\n",
       "      <th>stays_in_weekend_nights</th>\n",
       "      <th>stays_in_week_nights</th>\n",
       "      <th>adults</th>\n",
       "      <th>children</th>\n",
       "      <th>babies</th>\n",
       "      <th>meal</th>\n",
       "      <th>country</th>\n",
       "      <th>market_segment</th>\n",
       "      <th>distribution_channel</th>\n",
       "      <th>is_repeated_guest</th>\n",
       "      <th>previous_cancellations</th>\n",
       "      <th>previous_bookings_not_canceled</th>\n",
       "      <th>reserved_room_type</th>\n",
       "      <th>assigned_room_type</th>\n",
       "      <th>booking_changes</th>\n",
       "      <th>deposit_type</th>\n",
       "      <th>agent</th>\n",
       "      <th>company</th>\n",
       "      <th>days_in_waiting_list</th>\n",
       "      <th>customer_type</th>\n",
       "      <th>adr</th>\n",
       "      <th>required_car_parking_spaces</th>\n",
       "      <th>total_of_special_requests</th>\n",
       "      <th>reservation_status</th>\n",
       "      <th>reservation_status_date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>0</td>\n",
       "      <td>342</td>\n",
       "      <td>2015</td>\n",
       "      <td>July</td>\n",
       "      <td>27</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>BB</td>\n",
       "      <td>PRT</td>\n",
       "      <td>Direct</td>\n",
       "      <td>Direct</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>C</td>\n",
       "      <td>C</td>\n",
       "      <td>3</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Transient</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Check-Out</td>\n",
       "      <td>7/1/2015</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>0</td>\n",
       "      <td>737</td>\n",
       "      <td>2015</td>\n",
       "      <td>July</td>\n",
       "      <td>27</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>BB</td>\n",
       "      <td>PRT</td>\n",
       "      <td>Direct</td>\n",
       "      <td>Direct</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>C</td>\n",
       "      <td>C</td>\n",
       "      <td>4</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Transient</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Check-Out</td>\n",
       "      <td>7/1/2015</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>0</td>\n",
       "      <td>7</td>\n",
       "      <td>2015</td>\n",
       "      <td>July</td>\n",
       "      <td>27</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>BB</td>\n",
       "      <td>GBR</td>\n",
       "      <td>Direct</td>\n",
       "      <td>Direct</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>A</td>\n",
       "      <td>C</td>\n",
       "      <td>0</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Transient</td>\n",
       "      <td>75.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Check-Out</td>\n",
       "      <td>7/2/2015</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>0</td>\n",
       "      <td>13</td>\n",
       "      <td>2015</td>\n",
       "      <td>July</td>\n",
       "      <td>27</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>BB</td>\n",
       "      <td>GBR</td>\n",
       "      <td>Corporate</td>\n",
       "      <td>Corporate</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>A</td>\n",
       "      <td>A</td>\n",
       "      <td>0</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>304.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Transient</td>\n",
       "      <td>75.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Check-Out</td>\n",
       "      <td>7/2/2015</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>0</td>\n",
       "      <td>14</td>\n",
       "      <td>2015</td>\n",
       "      <td>July</td>\n",
       "      <td>27</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>BB</td>\n",
       "      <td>GBR</td>\n",
       "      <td>Online TA</td>\n",
       "      <td>TA/TO</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>A</td>\n",
       "      <td>A</td>\n",
       "      <td>0</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>240.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Transient</td>\n",
       "      <td>98.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>Check-Out</td>\n",
       "      <td>7/3/2015</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          hotel  is_canceled  lead_time  arrival_date_year arrival_date_month  \\\n",
       "0  Resort Hotel            0        342               2015               July   \n",
       "1  Resort Hotel            0        737               2015               July   \n",
       "2  Resort Hotel            0          7               2015               July   \n",
       "3  Resort Hotel            0         13               2015               July   \n",
       "4  Resort Hotel            0         14               2015               July   \n",
       "\n",
       "   arrival_date_week_number  arrival_date_day_of_month  \\\n",
       "0                        27                          1   \n",
       "1                        27                          1   \n",
       "2                        27                          1   \n",
       "3                        27                          1   \n",
       "4                        27                          1   \n",
       "\n",
       "   stays_in_weekend_nights  stays_in_week_nights  adults  children  babies  \\\n",
       "0                        0                     0       2       0.0       0   \n",
       "1                        0                     0       2       0.0       0   \n",
       "2                        0                     1       1       0.0       0   \n",
       "3                        0                     1       1       0.0       0   \n",
       "4                        0                     2       2       0.0       0   \n",
       "\n",
       "  meal country market_segment distribution_channel  is_repeated_guest  \\\n",
       "0   BB     PRT         Direct               Direct                  0   \n",
       "1   BB     PRT         Direct               Direct                  0   \n",
       "2   BB     GBR         Direct               Direct                  0   \n",
       "3   BB     GBR      Corporate            Corporate                  0   \n",
       "4   BB     GBR      Online TA                TA/TO                  0   \n",
       "\n",
       "   previous_cancellations  previous_bookings_not_canceled reserved_room_type  \\\n",
       "0                       0                               0                  C   \n",
       "1                       0                               0                  C   \n",
       "2                       0                               0                  A   \n",
       "3                       0                               0                  A   \n",
       "4                       0                               0                  A   \n",
       "\n",
       "  assigned_room_type  booking_changes deposit_type  agent  company  \\\n",
       "0                  C                3   No Deposit    0.0      0.0   \n",
       "1                  C                4   No Deposit    0.0      0.0   \n",
       "2                  C                0   No Deposit    0.0      0.0   \n",
       "3                  A                0   No Deposit  304.0      0.0   \n",
       "4                  A                0   No Deposit  240.0      0.0   \n",
       "\n",
       "   days_in_waiting_list customer_type   adr  required_car_parking_spaces  \\\n",
       "0                     0     Transient   0.0                            0   \n",
       "1                     0     Transient   0.0                            0   \n",
       "2                     0     Transient  75.0                            0   \n",
       "3                     0     Transient  75.0                            0   \n",
       "4                     0     Transient  98.0                            0   \n",
       "\n",
       "   total_of_special_requests reservation_status reservation_status_date  \n",
       "0                          0          Check-Out                7/1/2015  \n",
       "1                          0          Check-Out                7/1/2015  \n",
       "2                          0          Check-Out                7/2/2015  \n",
       "3                          0          Check-Out                7/2/2015  \n",
       "4                          1          Check-Out                7/3/2015  "
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "301d203c",
   "metadata": {},
   "outputs": [],
   "source": [
    "data2=data[data['is_canceled']==0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "25e4d461",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 864x576 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(12,8))\n",
    "sns.boxplot(x='reserved_room_type',y='adr',hue='hotel',data=data2)\n",
    "plt.title('price of room types per night and per person')\n",
    "plt.xlabel('Room type')\n",
    "plt.ylabel('price(Euro)')\n",
    "plt.legend()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "3e8918ae",
   "metadata": {},
   "outputs": [],
   "source": [
    "data_resort=data[(data['hotel']=='Resort Hotel') & (data['is_canceled']==0)]\n",
    "data_city=data[(data['hotel']=='City Hotel') & (data['is_canceled']==0)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "203177b3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>hotel</th>\n",
       "      <th>is_canceled</th>\n",
       "      <th>lead_time</th>\n",
       "      <th>arrival_date_year</th>\n",
       "      <th>arrival_date_month</th>\n",
       "      <th>arrival_date_week_number</th>\n",
       "      <th>arrival_date_day_of_month</th>\n",
       "      <th>stays_in_weekend_nights</th>\n",
       "      <th>stays_in_week_nights</th>\n",
       "      <th>adults</th>\n",
       "      <th>children</th>\n",
       "      <th>babies</th>\n",
       "      <th>meal</th>\n",
       "      <th>country</th>\n",
       "      <th>market_segment</th>\n",
       "      <th>distribution_channel</th>\n",
       "      <th>is_repeated_guest</th>\n",
       "      <th>previous_cancellations</th>\n",
       "      <th>previous_bookings_not_canceled</th>\n",
       "      <th>reserved_room_type</th>\n",
       "      <th>assigned_room_type</th>\n",
       "      <th>booking_changes</th>\n",
       "      <th>deposit_type</th>\n",
       "      <th>agent</th>\n",
       "      <th>company</th>\n",
       "      <th>days_in_waiting_list</th>\n",
       "      <th>customer_type</th>\n",
       "      <th>adr</th>\n",
       "      <th>required_car_parking_spaces</th>\n",
       "      <th>total_of_special_requests</th>\n",
       "      <th>reservation_status</th>\n",
       "      <th>reservation_status_date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>0</td>\n",
       "      <td>342</td>\n",
       "      <td>2015</td>\n",
       "      <td>July</td>\n",
       "      <td>27</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>BB</td>\n",
       "      <td>PRT</td>\n",
       "      <td>Direct</td>\n",
       "      <td>Direct</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>C</td>\n",
       "      <td>C</td>\n",
       "      <td>3</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Transient</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Check-Out</td>\n",
       "      <td>7/1/2015</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>0</td>\n",
       "      <td>737</td>\n",
       "      <td>2015</td>\n",
       "      <td>July</td>\n",
       "      <td>27</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>BB</td>\n",
       "      <td>PRT</td>\n",
       "      <td>Direct</td>\n",
       "      <td>Direct</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>C</td>\n",
       "      <td>C</td>\n",
       "      <td>4</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Transient</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Check-Out</td>\n",
       "      <td>7/1/2015</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>0</td>\n",
       "      <td>7</td>\n",
       "      <td>2015</td>\n",
       "      <td>July</td>\n",
       "      <td>27</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>BB</td>\n",
       "      <td>GBR</td>\n",
       "      <td>Direct</td>\n",
       "      <td>Direct</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>A</td>\n",
       "      <td>C</td>\n",
       "      <td>0</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Transient</td>\n",
       "      <td>75.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Check-Out</td>\n",
       "      <td>7/2/2015</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>0</td>\n",
       "      <td>13</td>\n",
       "      <td>2015</td>\n",
       "      <td>July</td>\n",
       "      <td>27</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>BB</td>\n",
       "      <td>GBR</td>\n",
       "      <td>Corporate</td>\n",
       "      <td>Corporate</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>A</td>\n",
       "      <td>A</td>\n",
       "      <td>0</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>304.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Transient</td>\n",
       "      <td>75.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Check-Out</td>\n",
       "      <td>7/2/2015</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>0</td>\n",
       "      <td>14</td>\n",
       "      <td>2015</td>\n",
       "      <td>July</td>\n",
       "      <td>27</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>BB</td>\n",
       "      <td>GBR</td>\n",
       "      <td>Online TA</td>\n",
       "      <td>TA/TO</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>A</td>\n",
       "      <td>A</td>\n",
       "      <td>0</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>240.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Transient</td>\n",
       "      <td>98.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>Check-Out</td>\n",
       "      <td>7/3/2015</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          hotel  is_canceled  lead_time  arrival_date_year arrival_date_month  \\\n",
       "0  Resort Hotel            0        342               2015               July   \n",
       "1  Resort Hotel            0        737               2015               July   \n",
       "2  Resort Hotel            0          7               2015               July   \n",
       "3  Resort Hotel            0         13               2015               July   \n",
       "4  Resort Hotel            0         14               2015               July   \n",
       "\n",
       "   arrival_date_week_number  arrival_date_day_of_month  \\\n",
       "0                        27                          1   \n",
       "1                        27                          1   \n",
       "2                        27                          1   \n",
       "3                        27                          1   \n",
       "4                        27                          1   \n",
       "\n",
       "   stays_in_weekend_nights  stays_in_week_nights  adults  children  babies  \\\n",
       "0                        0                     0       2       0.0       0   \n",
       "1                        0                     0       2       0.0       0   \n",
       "2                        0                     1       1       0.0       0   \n",
       "3                        0                     1       1       0.0       0   \n",
       "4                        0                     2       2       0.0       0   \n",
       "\n",
       "  meal country market_segment distribution_channel  is_repeated_guest  \\\n",
       "0   BB     PRT         Direct               Direct                  0   \n",
       "1   BB     PRT         Direct               Direct                  0   \n",
       "2   BB     GBR         Direct               Direct                  0   \n",
       "3   BB     GBR      Corporate            Corporate                  0   \n",
       "4   BB     GBR      Online TA                TA/TO                  0   \n",
       "\n",
       "   previous_cancellations  previous_bookings_not_canceled reserved_room_type  \\\n",
       "0                       0                               0                  C   \n",
       "1                       0                               0                  C   \n",
       "2                       0                               0                  A   \n",
       "3                       0                               0                  A   \n",
       "4                       0                               0                  A   \n",
       "\n",
       "  assigned_room_type  booking_changes deposit_type  agent  company  \\\n",
       "0                  C                3   No Deposit    0.0      0.0   \n",
       "1                  C                4   No Deposit    0.0      0.0   \n",
       "2                  C                0   No Deposit    0.0      0.0   \n",
       "3                  A                0   No Deposit  304.0      0.0   \n",
       "4                  A                0   No Deposit  240.0      0.0   \n",
       "\n",
       "   days_in_waiting_list customer_type   adr  required_car_parking_spaces  \\\n",
       "0                     0     Transient   0.0                            0   \n",
       "1                     0     Transient   0.0                            0   \n",
       "2                     0     Transient  75.0                            0   \n",
       "3                     0     Transient  75.0                            0   \n",
       "4                     0     Transient  98.0                            0   \n",
       "\n",
       "   total_of_special_requests reservation_status reservation_status_date  \n",
       "0                          0          Check-Out                7/1/2015  \n",
       "1                          0          Check-Out                7/1/2015  \n",
       "2                          0          Check-Out                7/2/2015  \n",
       "3                          0          Check-Out                7/2/2015  \n",
       "4                          1          Check-Out                7/3/2015  "
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_resort.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "f790a0ad",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>arrival_date_month</th>\n",
       "      <th>adr</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>April</td>\n",
       "      <td>75.867816</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>August</td>\n",
       "      <td>181.205892</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>December</td>\n",
       "      <td>68.410104</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>February</td>\n",
       "      <td>54.147478</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>January</td>\n",
       "      <td>48.761125</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>July</td>\n",
       "      <td>150.122528</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>June</td>\n",
       "      <td>107.974850</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>March</td>\n",
       "      <td>57.056838</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>May</td>\n",
       "      <td>76.657558</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>November</td>\n",
       "      <td>48.706289</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>October</td>\n",
       "      <td>61.775449</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>September</td>\n",
       "      <td>96.416860</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   arrival_date_month         adr\n",
       "0               April   75.867816\n",
       "1              August  181.205892\n",
       "2            December   68.410104\n",
       "3            February   54.147478\n",
       "4             January   48.761125\n",
       "5                July  150.122528\n",
       "6                June  107.974850\n",
       "7               March   57.056838\n",
       "8                 May   76.657558\n",
       "9            November   48.706289\n",
       "10            October   61.775449\n",
       "11          September   96.416860"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "resort_hotel=data_resort.groupby(['arrival_date_month'])['adr'].mean().reset_index()\n",
    "resort_hotel"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "408d2014",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>arrival_date_month</th>\n",
       "      <th>adr</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>April</td>\n",
       "      <td>111.962267</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>August</td>\n",
       "      <td>118.674598</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>December</td>\n",
       "      <td>88.401855</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>February</td>\n",
       "      <td>86.520062</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>January</td>\n",
       "      <td>82.330983</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>July</td>\n",
       "      <td>115.818019</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>June</td>\n",
       "      <td>117.874360</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>March</td>\n",
       "      <td>90.658533</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>May</td>\n",
       "      <td>120.669827</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>November</td>\n",
       "      <td>86.946592</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>October</td>\n",
       "      <td>102.004672</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>September</td>\n",
       "      <td>112.776582</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   arrival_date_month         adr\n",
       "0               April  111.962267\n",
       "1              August  118.674598\n",
       "2            December   88.401855\n",
       "3            February   86.520062\n",
       "4             January   82.330983\n",
       "5                July  115.818019\n",
       "6                June  117.874360\n",
       "7               March   90.658533\n",
       "8                 May  120.669827\n",
       "9            November   86.946592\n",
       "10            October  102.004672\n",
       "11          September  112.776582"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "city_hotel=data_city.groupby(['arrival_date_month'])['adr'].mean().reset_index()\n",
    "city_hotel"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "8831e9db",
   "metadata": {},
   "outputs": [],
   "source": [
    "final=resort_hotel.merge(city_hotel,on='arrival_date_month')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "896fc33d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>month</th>\n",
       "      <th>price_for _resort</th>\n",
       "      <th>priice_for_city_hotel</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>April</td>\n",
       "      <td>75.867816</td>\n",
       "      <td>111.962267</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>August</td>\n",
       "      <td>181.205892</td>\n",
       "      <td>118.674598</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>December</td>\n",
       "      <td>68.410104</td>\n",
       "      <td>88.401855</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>February</td>\n",
       "      <td>54.147478</td>\n",
       "      <td>86.520062</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>January</td>\n",
       "      <td>48.761125</td>\n",
       "      <td>82.330983</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>July</td>\n",
       "      <td>150.122528</td>\n",
       "      <td>115.818019</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>June</td>\n",
       "      <td>107.974850</td>\n",
       "      <td>117.874360</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>March</td>\n",
       "      <td>57.056838</td>\n",
       "      <td>90.658533</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>May</td>\n",
       "      <td>76.657558</td>\n",
       "      <td>120.669827</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>November</td>\n",
       "      <td>48.706289</td>\n",
       "      <td>86.946592</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>October</td>\n",
       "      <td>61.775449</td>\n",
       "      <td>102.004672</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>September</td>\n",
       "      <td>96.416860</td>\n",
       "      <td>112.776582</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        month  price_for _resort  priice_for_city_hotel\n",
       "0       April          75.867816             111.962267\n",
       "1      August         181.205892             118.674598\n",
       "2    December          68.410104              88.401855\n",
       "3    February          54.147478              86.520062\n",
       "4     January          48.761125              82.330983\n",
       "5        July         150.122528             115.818019\n",
       "6        June         107.974850             117.874360\n",
       "7       March          57.056838              90.658533\n",
       "8         May          76.657558             120.669827\n",
       "9    November          48.706289              86.946592\n",
       "10    October          61.775449             102.004672\n",
       "11  September          96.416860             112.776582"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "final.columns=['month','price_for _resort','priice_for_city_hotel']\n",
    "final"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "936adb81",
   "metadata": {},
   "outputs": [],
   "source": [
    "import sort_dataframeby_monthorweek as sd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "eb275b2f",
   "metadata": {},
   "outputs": [],
   "source": [
    "def sort_data(df,colname):\n",
    "    return sd.Sort_Dataframeby_Month(df,colname)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "27c01268",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>month</th>\n",
       "      <th>price_for _resort</th>\n",
       "      <th>priice_for_city_hotel</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>January</td>\n",
       "      <td>48.761125</td>\n",
       "      <td>82.330983</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>February</td>\n",
       "      <td>54.147478</td>\n",
       "      <td>86.520062</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>March</td>\n",
       "      <td>57.056838</td>\n",
       "      <td>90.658533</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>April</td>\n",
       "      <td>75.867816</td>\n",
       "      <td>111.962267</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>May</td>\n",
       "      <td>76.657558</td>\n",
       "      <td>120.669827</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>June</td>\n",
       "      <td>107.974850</td>\n",
       "      <td>117.874360</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>July</td>\n",
       "      <td>150.122528</td>\n",
       "      <td>115.818019</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>August</td>\n",
       "      <td>181.205892</td>\n",
       "      <td>118.674598</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>September</td>\n",
       "      <td>96.416860</td>\n",
       "      <td>112.776582</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>October</td>\n",
       "      <td>61.775449</td>\n",
       "      <td>102.004672</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>November</td>\n",
       "      <td>48.706289</td>\n",
       "      <td>86.946592</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>December</td>\n",
       "      <td>68.410104</td>\n",
       "      <td>88.401855</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        month  price_for _resort  priice_for_city_hotel\n",
       "0     January          48.761125              82.330983\n",
       "1    February          54.147478              86.520062\n",
       "2       March          57.056838              90.658533\n",
       "3       April          75.867816             111.962267\n",
       "4         May          76.657558             120.669827\n",
       "5        June         107.974850             117.874360\n",
       "6        July         150.122528             115.818019\n",
       "7      August         181.205892             118.674598\n",
       "8   September          96.416860             112.776582\n",
       "9     October          61.775449             102.004672\n",
       "10   November          48.706289              86.946592\n",
       "11   December          68.410104              88.401855"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "final=sort_data(final,'month')\n",
    "final"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "16176b31",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['month', 'price_for _resort', 'priice_for_city_hotel'], dtype='object')"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "final.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "0a1f12a8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "hovertemplate": "variable=price_for _resort<br>month=%{x}<br>value=%{y}<extra></extra>",
         "legendgroup": "price_for _resort",
         "line": {
          "color": "#636efa",
          "dash": "solid"
         },
         "mode": "lines",
         "name": "price_for _resort",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
          "September",
          "October",
          "November",
          "December"
         ],
         "xaxis": "x",
         "y": [
          48.76112540192932,
          54.14747833622187,
          57.056837806301175,
          75.86781568627462,
          76.65755818540472,
          107.97485027000545,
          150.12252789289084,
          181.205891925084,
          96.4168601332064,
          61.77544854368931,
          48.706288607595184,
          68.41010427010937
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "variable=priice_for_city_hotel<br>month=%{x}<br>value=%{y}<extra></extra>",
         "legendgroup": "priice_for_city_hotel",
         "line": {
          "color": "#EF553B",
          "dash": "solid"
         },
         "mode": "lines",
         "name": "priice_for_city_hotel",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
          "September",
          "October",
          "November",
          "December"
         ],
         "xaxis": "x",
         "y": [
          82.33098265895951,
          86.52006227466379,
          90.65853297110417,
          111.96226683291741,
          120.66982705779294,
          117.87435979807228,
          115.81801886792235,
          118.6745984721439,
          112.77658183516273,
          102.00467175219605,
          86.94659192825135,
          88.40185527976439
         ],
         "yaxis": "y"
        }
       ],
       "layout": {
        "legend": {
         "title": {
          "text": "variable"
         },
         "tracegroupgap": 0
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "room price per night over the month"
        },
        "xaxis": {
         "anchor": "y",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": "month"
         }
        },
        "yaxis": {
         "anchor": "x",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": "value"
         }
        }
       }
      },
      "text/html": [
       "<div>                            <div id=\"eafc59d9-5a08-419f-81a4-b718228357e6\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"eafc59d9-5a08-419f-81a4-b718228357e6\")) {                    Plotly.newPlot(                        \"eafc59d9-5a08-419f-81a4-b718228357e6\",                        [{\"hovertemplate\":\"variable=price_for _resort<br>month=%{x}<br>value=%{y}<extra></extra>\",\"legendgroup\":\"price_for _resort\",\"line\":{\"color\":\"#636efa\",\"dash\":\"solid\"},\"mode\":\"lines\",\"name\":\"price_for _resort\",\"orientation\":\"v\",\"showlegend\":true,\"type\":\"scatter\",\"x\":[\"January\",\"February\",\"March\",\"April\",\"May\",\"June\",\"July\",\"August\",\"September\",\"October\",\"November\",\"December\"],\"xaxis\":\"x\",\"y\":[48.76112540192932,54.14747833622187,57.056837806301175,75.86781568627462,76.65755818540472,107.97485027000545,150.12252789289084,181.205891925084,96.4168601332064,61.77544854368931,48.706288607595184,68.41010427010937],\"yaxis\":\"y\"},{\"hovertemplate\":\"variable=priice_for_city_hotel<br>month=%{x}<br>value=%{y}<extra></extra>\",\"legendgroup\":\"priice_for_city_hotel\",\"line\":{\"color\":\"#EF553B\",\"dash\":\"solid\"},\"mode\":\"lines\",\"name\":\"priice_for_city_hotel\",\"orientation\":\"v\",\"showlegend\":true,\"type\":\"scatter\",\"x\":[\"January\",\"February\",\"March\",\"April\",\"May\",\"June\",\"July\",\"August\",\"September\",\"October\",\"November\",\"December\"],\"xaxis\":\"x\",\"y\":[82.33098265895951,86.52006227466379,90.65853297110417,111.96226683291741,120.66982705779294,117.87435979807228,115.81801886792235,118.6745984721439,112.77658183516273,102.00467175219605,86.94659192825135,88.40185527976439],\"yaxis\":\"y\"}],                        {\"legend\":{\"title\":{\"text\":\"variable\"},\"tracegroupgap\":0},\"template\":{\"data\":{\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"choropleth\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"choropleth\"}],\"contour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"contour\"}],\"contourcarpet\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"contourcarpet\"}],\"heatmap\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmap\"}],\"heatmapgl\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmapgl\"}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"histogram2d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2d\"}],\"histogram2dcontour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2dcontour\"}],\"mesh3d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"mesh3d\"}],\"parcoords\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"parcoords\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}],\"scatter\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter\"}],\"scatter3d\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter3d\"}],\"scattercarpet\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattercarpet\"}],\"scattergeo\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergeo\"}],\"scattergl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergl\"}],\"scattermapbox\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattermapbox\"}],\"scatterpolar\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolar\"}],\"scatterpolargl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolargl\"}],\"scatterternary\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterternary\"}],\"surface\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"surface\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}]},\"layout\":{\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"autotypenumbers\":\"strict\",\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]],\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]},\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"geo\":{\"bgcolor\":\"white\",\"lakecolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"showlakes\":true,\"showland\":true,\"subunitcolor\":\"white\"},\"hoverlabel\":{\"align\":\"left\"},\"hovermode\":\"closest\",\"mapbox\":{\"style\":\"light\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"ternary\":{\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"title\":{\"x\":0.05},\"xaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2},\"yaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2}}},\"title\":{\"text\":\"room price per night over the month\"},\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"month\"}},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"value\"}}},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('eafc59d9-5a08-419f-81a4-b718228357e6');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "px.line(final,x='month',y=['price_for _resort', 'priice_for_city_hotel'],title='room price per night over the month')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "1f95d3e5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>hotel</th>\n",
       "      <th>is_canceled</th>\n",
       "      <th>lead_time</th>\n",
       "      <th>arrival_date_year</th>\n",
       "      <th>arrival_date_month</th>\n",
       "      <th>arrival_date_week_number</th>\n",
       "      <th>arrival_date_day_of_month</th>\n",
       "      <th>stays_in_weekend_nights</th>\n",
       "      <th>stays_in_week_nights</th>\n",
       "      <th>adults</th>\n",
       "      <th>children</th>\n",
       "      <th>babies</th>\n",
       "      <th>meal</th>\n",
       "      <th>country</th>\n",
       "      <th>market_segment</th>\n",
       "      <th>distribution_channel</th>\n",
       "      <th>is_repeated_guest</th>\n",
       "      <th>previous_cancellations</th>\n",
       "      <th>previous_bookings_not_canceled</th>\n",
       "      <th>reserved_room_type</th>\n",
       "      <th>assigned_room_type</th>\n",
       "      <th>booking_changes</th>\n",
       "      <th>deposit_type</th>\n",
       "      <th>agent</th>\n",
       "      <th>company</th>\n",
       "      <th>days_in_waiting_list</th>\n",
       "      <th>customer_type</th>\n",
       "      <th>adr</th>\n",
       "      <th>required_car_parking_spaces</th>\n",
       "      <th>total_of_special_requests</th>\n",
       "      <th>reservation_status</th>\n",
       "      <th>reservation_status_date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>0</td>\n",
       "      <td>342</td>\n",
       "      <td>2015</td>\n",
       "      <td>July</td>\n",
       "      <td>27</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>BB</td>\n",
       "      <td>PRT</td>\n",
       "      <td>Direct</td>\n",
       "      <td>Direct</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>C</td>\n",
       "      <td>C</td>\n",
       "      <td>3</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Transient</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Check-Out</td>\n",
       "      <td>7/1/2015</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>0</td>\n",
       "      <td>737</td>\n",
       "      <td>2015</td>\n",
       "      <td>July</td>\n",
       "      <td>27</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>BB</td>\n",
       "      <td>PRT</td>\n",
       "      <td>Direct</td>\n",
       "      <td>Direct</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>C</td>\n",
       "      <td>C</td>\n",
       "      <td>4</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Transient</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Check-Out</td>\n",
       "      <td>7/1/2015</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>0</td>\n",
       "      <td>7</td>\n",
       "      <td>2015</td>\n",
       "      <td>July</td>\n",
       "      <td>27</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>BB</td>\n",
       "      <td>GBR</td>\n",
       "      <td>Direct</td>\n",
       "      <td>Direct</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>A</td>\n",
       "      <td>C</td>\n",
       "      <td>0</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Transient</td>\n",
       "      <td>75.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Check-Out</td>\n",
       "      <td>7/2/2015</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>0</td>\n",
       "      <td>13</td>\n",
       "      <td>2015</td>\n",
       "      <td>July</td>\n",
       "      <td>27</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>BB</td>\n",
       "      <td>GBR</td>\n",
       "      <td>Corporate</td>\n",
       "      <td>Corporate</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>A</td>\n",
       "      <td>A</td>\n",
       "      <td>0</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>304.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Transient</td>\n",
       "      <td>75.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Check-Out</td>\n",
       "      <td>7/2/2015</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>0</td>\n",
       "      <td>14</td>\n",
       "      <td>2015</td>\n",
       "      <td>July</td>\n",
       "      <td>27</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>BB</td>\n",
       "      <td>GBR</td>\n",
       "      <td>Online TA</td>\n",
       "      <td>TA/TO</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>A</td>\n",
       "      <td>A</td>\n",
       "      <td>0</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>240.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Transient</td>\n",
       "      <td>98.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>Check-Out</td>\n",
       "      <td>7/3/2015</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          hotel  is_canceled  lead_time  arrival_date_year arrival_date_month  \\\n",
       "0  Resort Hotel            0        342               2015               July   \n",
       "1  Resort Hotel            0        737               2015               July   \n",
       "2  Resort Hotel            0          7               2015               July   \n",
       "3  Resort Hotel            0         13               2015               July   \n",
       "4  Resort Hotel            0         14               2015               July   \n",
       "\n",
       "   arrival_date_week_number  arrival_date_day_of_month  \\\n",
       "0                        27                          1   \n",
       "1                        27                          1   \n",
       "2                        27                          1   \n",
       "3                        27                          1   \n",
       "4                        27                          1   \n",
       "\n",
       "   stays_in_weekend_nights  stays_in_week_nights  adults  children  babies  \\\n",
       "0                        0                     0       2       0.0       0   \n",
       "1                        0                     0       2       0.0       0   \n",
       "2                        0                     1       1       0.0       0   \n",
       "3                        0                     1       1       0.0       0   \n",
       "4                        0                     2       2       0.0       0   \n",
       "\n",
       "  meal country market_segment distribution_channel  is_repeated_guest  \\\n",
       "0   BB     PRT         Direct               Direct                  0   \n",
       "1   BB     PRT         Direct               Direct                  0   \n",
       "2   BB     GBR         Direct               Direct                  0   \n",
       "3   BB     GBR      Corporate            Corporate                  0   \n",
       "4   BB     GBR      Online TA                TA/TO                  0   \n",
       "\n",
       "   previous_cancellations  previous_bookings_not_canceled reserved_room_type  \\\n",
       "0                       0                               0                  C   \n",
       "1                       0                               0                  C   \n",
       "2                       0                               0                  A   \n",
       "3                       0                               0                  A   \n",
       "4                       0                               0                  A   \n",
       "\n",
       "  assigned_room_type  booking_changes deposit_type  agent  company  \\\n",
       "0                  C                3   No Deposit    0.0      0.0   \n",
       "1                  C                4   No Deposit    0.0      0.0   \n",
       "2                  C                0   No Deposit    0.0      0.0   \n",
       "3                  A                0   No Deposit  304.0      0.0   \n",
       "4                  A                0   No Deposit  240.0      0.0   \n",
       "\n",
       "   days_in_waiting_list customer_type   adr  required_car_parking_spaces  \\\n",
       "0                     0     Transient   0.0                            0   \n",
       "1                     0     Transient   0.0                            0   \n",
       "2                     0     Transient  75.0                            0   \n",
       "3                     0     Transient  75.0                            0   \n",
       "4                     0     Transient  98.0                            0   \n",
       "\n",
       "   total_of_special_requests reservation_status reservation_status_date  \n",
       "0                          0          Check-Out                7/1/2015  \n",
       "1                          0          Check-Out                7/1/2015  \n",
       "2                          0          Check-Out                7/2/2015  \n",
       "3                          0          Check-Out                7/2/2015  \n",
       "4                          1          Check-Out                7/3/2015  "
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_resort.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "6c739480",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>month</th>\n",
       "      <th>no. of guests</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>August</td>\n",
       "      <td>3257</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>July</td>\n",
       "      <td>3137</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>October</td>\n",
       "      <td>2575</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>March</td>\n",
       "      <td>2571</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>April</td>\n",
       "      <td>2550</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>May</td>\n",
       "      <td>2535</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>February</td>\n",
       "      <td>2308</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>September</td>\n",
       "      <td>2102</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>June</td>\n",
       "      <td>2037</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>December</td>\n",
       "      <td>2014</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>November</td>\n",
       "      <td>1975</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>January</td>\n",
       "      <td>1866</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        month  no. of guests\n",
       "0      August           3257\n",
       "1        July           3137\n",
       "2     October           2575\n",
       "3       March           2571\n",
       "4       April           2550\n",
       "5         May           2535\n",
       "6    February           2308\n",
       "7   September           2102\n",
       "8        June           2037\n",
       "9    December           2014\n",
       "10   November           1975\n",
       "11    January           1866"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rush_resort=data_resort['arrival_date_month'].value_counts().reset_index()\n",
    "rush_resort.columns=['month','no. of guests']\n",
    "rush_resort"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "e76607ad",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>month</th>\n",
       "      <th>no. of guests</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>August</td>\n",
       "      <td>5367</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>July</td>\n",
       "      <td>4770</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>May</td>\n",
       "      <td>4568</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>June</td>\n",
       "      <td>4358</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>October</td>\n",
       "      <td>4326</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>September</td>\n",
       "      <td>4283</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>March</td>\n",
       "      <td>4049</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>April</td>\n",
       "      <td>4010</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>February</td>\n",
       "      <td>3051</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>November</td>\n",
       "      <td>2676</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>December</td>\n",
       "      <td>2377</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>January</td>\n",
       "      <td>2249</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        month  no. of guests\n",
       "0      August           5367\n",
       "1        July           4770\n",
       "2         May           4568\n",
       "3        June           4358\n",
       "4     October           4326\n",
       "5   September           4283\n",
       "6       March           4049\n",
       "7       April           4010\n",
       "8    February           3051\n",
       "9    November           2676\n",
       "10   December           2377\n",
       "11    January           2249"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rush_city=data_city['arrival_date_month'].value_counts().reset_index()\n",
    "rush_city.columns=['month','no. of guests']\n",
    "rush_city"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "576a95c0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>month</th>\n",
       "      <th>no. of guests in resort</th>\n",
       "      <th>no. of guests in city</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>August</td>\n",
       "      <td>3257</td>\n",
       "      <td>5367</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>July</td>\n",
       "      <td>3137</td>\n",
       "      <td>4770</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>October</td>\n",
       "      <td>2575</td>\n",
       "      <td>4326</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>March</td>\n",
       "      <td>2571</td>\n",
       "      <td>4049</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>April</td>\n",
       "      <td>2550</td>\n",
       "      <td>4010</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>May</td>\n",
       "      <td>2535</td>\n",
       "      <td>4568</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>February</td>\n",
       "      <td>2308</td>\n",
       "      <td>3051</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>September</td>\n",
       "      <td>2102</td>\n",
       "      <td>4283</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>June</td>\n",
       "      <td>2037</td>\n",
       "      <td>4358</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>December</td>\n",
       "      <td>2014</td>\n",
       "      <td>2377</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>November</td>\n",
       "      <td>1975</td>\n",
       "      <td>2676</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>January</td>\n",
       "      <td>1866</td>\n",
       "      <td>2249</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        month  no. of guests in resort  no. of guests in city\n",
       "0      August                     3257                   5367\n",
       "1        July                     3137                   4770\n",
       "2     October                     2575                   4326\n",
       "3       March                     2571                   4049\n",
       "4       April                     2550                   4010\n",
       "5         May                     2535                   4568\n",
       "6    February                     2308                   3051\n",
       "7   September                     2102                   4283\n",
       "8        June                     2037                   4358\n",
       "9    December                     2014                   2377\n",
       "10   November                     1975                   2676\n",
       "11    January                     1866                   2249"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "final_rush=rush_resort.merge(rush_city,on='month')\n",
    "final_rush.columns=['month','no. of guests in resort','no. of guests in city']\n",
    "final_rush"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "03a55eb7",
   "metadata": {},
   "outputs": [],
   "source": [
    "final_rush=sort_data(final_rush,'month')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "c36a3470",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['month', 'no. of guests in resort', 'no. of guests in city'], dtype='object')"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "final_rush.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "415e8570",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "hovertemplate": "variable=no. of guests in resort<br>month=%{x}<br>value=%{y}<extra></extra>",
         "legendgroup": "no. of guests in resort",
         "line": {
          "color": "#636efa",
          "dash": "solid"
         },
         "mode": "lines",
         "name": "no. of guests in resort",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
          "September",
          "October",
          "November",
          "December"
         ],
         "xaxis": "x",
         "y": [
          1866,
          2308,
          2571,
          2550,
          2535,
          2037,
          3137,
          3257,
          2102,
          2575,
          1975,
          2014
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "variable=no. of guests in city<br>month=%{x}<br>value=%{y}<extra></extra>",
         "legendgroup": "no. of guests in city",
         "line": {
          "color": "#EF553B",
          "dash": "solid"
         },
         "mode": "lines",
         "name": "no. of guests in city",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
          "September",
          "October",
          "November",
          "December"
         ],
         "xaxis": "x",
         "y": [
          2249,
          3051,
          4049,
          4010,
          4568,
          4358,
          4770,
          5367,
          4283,
          4326,
          2676,
          2377
         ],
         "yaxis": "y"
        }
       ],
       "layout": {
        "legend": {
         "title": {
          "text": "variable"
         },
         "tracegroupgap": 0
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "total no. of guests per month"
        },
        "xaxis": {
         "anchor": "y",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": "month"
         }
        },
        "yaxis": {
         "anchor": "x",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": "value"
         }
        }
       }
      },
      "text/html": [
       "<div>                            <div id=\"1f39a382-7cda-48a0-b1f4-f44263153b2b\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"1f39a382-7cda-48a0-b1f4-f44263153b2b\")) {                    Plotly.newPlot(                        \"1f39a382-7cda-48a0-b1f4-f44263153b2b\",                        [{\"hovertemplate\":\"variable=no. of guests in resort<br>month=%{x}<br>value=%{y}<extra></extra>\",\"legendgroup\":\"no. of guests in resort\",\"line\":{\"color\":\"#636efa\",\"dash\":\"solid\"},\"mode\":\"lines\",\"name\":\"no. of guests in resort\",\"orientation\":\"v\",\"showlegend\":true,\"type\":\"scatter\",\"x\":[\"January\",\"February\",\"March\",\"April\",\"May\",\"June\",\"July\",\"August\",\"September\",\"October\",\"November\",\"December\"],\"xaxis\":\"x\",\"y\":[1866,2308,2571,2550,2535,2037,3137,3257,2102,2575,1975,2014],\"yaxis\":\"y\"},{\"hovertemplate\":\"variable=no. of guests in city<br>month=%{x}<br>value=%{y}<extra></extra>\",\"legendgroup\":\"no. of guests in city\",\"line\":{\"color\":\"#EF553B\",\"dash\":\"solid\"},\"mode\":\"lines\",\"name\":\"no. of guests in city\",\"orientation\":\"v\",\"showlegend\":true,\"type\":\"scatter\",\"x\":[\"January\",\"February\",\"March\",\"April\",\"May\",\"June\",\"July\",\"August\",\"September\",\"October\",\"November\",\"December\"],\"xaxis\":\"x\",\"y\":[2249,3051,4049,4010,4568,4358,4770,5367,4283,4326,2676,2377],\"yaxis\":\"y\"}],                        {\"legend\":{\"title\":{\"text\":\"variable\"},\"tracegroupgap\":0},\"template\":{\"data\":{\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"choropleth\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"choropleth\"}],\"contour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"contour\"}],\"contourcarpet\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"contourcarpet\"}],\"heatmap\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmap\"}],\"heatmapgl\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmapgl\"}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"histogram2d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2d\"}],\"histogram2dcontour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2dcontour\"}],\"mesh3d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"mesh3d\"}],\"parcoords\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"parcoords\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}],\"scatter\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter\"}],\"scatter3d\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter3d\"}],\"scattercarpet\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattercarpet\"}],\"scattergeo\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergeo\"}],\"scattergl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergl\"}],\"scattermapbox\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattermapbox\"}],\"scatterpolar\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolar\"}],\"scatterpolargl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolargl\"}],\"scatterternary\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterternary\"}],\"surface\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"surface\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}]},\"layout\":{\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"autotypenumbers\":\"strict\",\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]],\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]},\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"geo\":{\"bgcolor\":\"white\",\"lakecolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"showlakes\":true,\"showland\":true,\"subunitcolor\":\"white\"},\"hoverlabel\":{\"align\":\"left\"},\"hovermode\":\"closest\",\"mapbox\":{\"style\":\"light\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"ternary\":{\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"title\":{\"x\":0.05},\"xaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2},\"yaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2}}},\"title\":{\"text\":\"total no. of guests per month\"},\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"month\"}},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"value\"}}},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('1f39a382-7cda-48a0-b1f4-f44263153b2b');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "px.line(final_rush,x='month',y=['no. of guests in resort', 'no. of guests in city'],title='total no. of guests per month')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "1ab967ed",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>hotel</th>\n",
       "      <th>is_canceled</th>\n",
       "      <th>lead_time</th>\n",
       "      <th>arrival_date_year</th>\n",
       "      <th>arrival_date_month</th>\n",
       "      <th>arrival_date_week_number</th>\n",
       "      <th>arrival_date_day_of_month</th>\n",
       "      <th>stays_in_weekend_nights</th>\n",
       "      <th>stays_in_week_nights</th>\n",
       "      <th>adults</th>\n",
       "      <th>children</th>\n",
       "      <th>babies</th>\n",
       "      <th>meal</th>\n",
       "      <th>country</th>\n",
       "      <th>market_segment</th>\n",
       "      <th>distribution_channel</th>\n",
       "      <th>is_repeated_guest</th>\n",
       "      <th>previous_cancellations</th>\n",
       "      <th>previous_bookings_not_canceled</th>\n",
       "      <th>reserved_room_type</th>\n",
       "      <th>assigned_room_type</th>\n",
       "      <th>booking_changes</th>\n",
       "      <th>deposit_type</th>\n",
       "      <th>agent</th>\n",
       "      <th>company</th>\n",
       "      <th>days_in_waiting_list</th>\n",
       "      <th>customer_type</th>\n",
       "      <th>adr</th>\n",
       "      <th>required_car_parking_spaces</th>\n",
       "      <th>total_of_special_requests</th>\n",
       "      <th>reservation_status</th>\n",
       "      <th>reservation_status_date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>0</td>\n",
       "      <td>342</td>\n",
       "      <td>2015</td>\n",
       "      <td>July</td>\n",
       "      <td>27</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>BB</td>\n",
       "      <td>PRT</td>\n",
       "      <td>Direct</td>\n",
       "      <td>Direct</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>C</td>\n",
       "      <td>C</td>\n",
       "      <td>3</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Transient</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Check-Out</td>\n",
       "      <td>7/1/2015</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>0</td>\n",
       "      <td>737</td>\n",
       "      <td>2015</td>\n",
       "      <td>July</td>\n",
       "      <td>27</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>BB</td>\n",
       "      <td>PRT</td>\n",
       "      <td>Direct</td>\n",
       "      <td>Direct</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>C</td>\n",
       "      <td>C</td>\n",
       "      <td>4</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Transient</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Check-Out</td>\n",
       "      <td>7/1/2015</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>0</td>\n",
       "      <td>7</td>\n",
       "      <td>2015</td>\n",
       "      <td>July</td>\n",
       "      <td>27</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>BB</td>\n",
       "      <td>GBR</td>\n",
       "      <td>Direct</td>\n",
       "      <td>Direct</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>A</td>\n",
       "      <td>C</td>\n",
       "      <td>0</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Transient</td>\n",
       "      <td>75.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Check-Out</td>\n",
       "      <td>7/2/2015</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>0</td>\n",
       "      <td>13</td>\n",
       "      <td>2015</td>\n",
       "      <td>July</td>\n",
       "      <td>27</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>BB</td>\n",
       "      <td>GBR</td>\n",
       "      <td>Corporate</td>\n",
       "      <td>Corporate</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>A</td>\n",
       "      <td>A</td>\n",
       "      <td>0</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>304.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Transient</td>\n",
       "      <td>75.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Check-Out</td>\n",
       "      <td>7/2/2015</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>0</td>\n",
       "      <td>14</td>\n",
       "      <td>2015</td>\n",
       "      <td>July</td>\n",
       "      <td>27</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>BB</td>\n",
       "      <td>GBR</td>\n",
       "      <td>Online TA</td>\n",
       "      <td>TA/TO</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>A</td>\n",
       "      <td>A</td>\n",
       "      <td>0</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>240.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Transient</td>\n",
       "      <td>98.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>Check-Out</td>\n",
       "      <td>7/3/2015</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          hotel  is_canceled  lead_time  arrival_date_year arrival_date_month  \\\n",
       "0  Resort Hotel            0        342               2015               July   \n",
       "1  Resort Hotel            0        737               2015               July   \n",
       "2  Resort Hotel            0          7               2015               July   \n",
       "3  Resort Hotel            0         13               2015               July   \n",
       "4  Resort Hotel            0         14               2015               July   \n",
       "\n",
       "   arrival_date_week_number  arrival_date_day_of_month  \\\n",
       "0                        27                          1   \n",
       "1                        27                          1   \n",
       "2                        27                          1   \n",
       "3                        27                          1   \n",
       "4                        27                          1   \n",
       "\n",
       "   stays_in_weekend_nights  stays_in_week_nights  adults  children  babies  \\\n",
       "0                        0                     0       2       0.0       0   \n",
       "1                        0                     0       2       0.0       0   \n",
       "2                        0                     1       1       0.0       0   \n",
       "3                        0                     1       1       0.0       0   \n",
       "4                        0                     2       2       0.0       0   \n",
       "\n",
       "  meal country market_segment distribution_channel  is_repeated_guest  \\\n",
       "0   BB     PRT         Direct               Direct                  0   \n",
       "1   BB     PRT         Direct               Direct                  0   \n",
       "2   BB     GBR         Direct               Direct                  0   \n",
       "3   BB     GBR      Corporate            Corporate                  0   \n",
       "4   BB     GBR      Online TA                TA/TO                  0   \n",
       "\n",
       "   previous_cancellations  previous_bookings_not_canceled reserved_room_type  \\\n",
       "0                       0                               0                  C   \n",
       "1                       0                               0                  C   \n",
       "2                       0                               0                  A   \n",
       "3                       0                               0                  A   \n",
       "4                       0                               0                  A   \n",
       "\n",
       "  assigned_room_type  booking_changes deposit_type  agent  company  \\\n",
       "0                  C                3   No Deposit    0.0      0.0   \n",
       "1                  C                4   No Deposit    0.0      0.0   \n",
       "2                  C                0   No Deposit    0.0      0.0   \n",
       "3                  A                0   No Deposit  304.0      0.0   \n",
       "4                  A                0   No Deposit  240.0      0.0   \n",
       "\n",
       "   days_in_waiting_list customer_type   adr  required_car_parking_spaces  \\\n",
       "0                     0     Transient   0.0                            0   \n",
       "1                     0     Transient   0.0                            0   \n",
       "2                     0     Transient  75.0                            0   \n",
       "3                     0     Transient  75.0                            0   \n",
       "4                     0     Transient  98.0                            0   \n",
       "\n",
       "   total_of_special_requests reservation_status reservation_status_date  \n",
       "0                          0          Check-Out                7/1/2015  \n",
       "1                          0          Check-Out                7/1/2015  \n",
       "2                          0          Check-Out                7/2/2015  \n",
       "3                          0          Check-Out                7/2/2015  \n",
       "4                          1          Check-Out                7/3/2015  "
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "9911a5a7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>is_canceled</th>\n",
       "      <th>lead_time</th>\n",
       "      <th>arrival_date_year</th>\n",
       "      <th>arrival_date_week_number</th>\n",
       "      <th>arrival_date_day_of_month</th>\n",
       "      <th>stays_in_weekend_nights</th>\n",
       "      <th>stays_in_week_nights</th>\n",
       "      <th>adults</th>\n",
       "      <th>children</th>\n",
       "      <th>babies</th>\n",
       "      <th>is_repeated_guest</th>\n",
       "      <th>previous_cancellations</th>\n",
       "      <th>previous_bookings_not_canceled</th>\n",
       "      <th>booking_changes</th>\n",
       "      <th>agent</th>\n",
       "      <th>company</th>\n",
       "      <th>days_in_waiting_list</th>\n",
       "      <th>adr</th>\n",
       "      <th>required_car_parking_spaces</th>\n",
       "      <th>total_of_special_requests</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>is_canceled</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.292876</td>\n",
       "      <td>0.016622</td>\n",
       "      <td>0.008315</td>\n",
       "      <td>-0.005948</td>\n",
       "      <td>-0.001323</td>\n",
       "      <td>0.025542</td>\n",
       "      <td>0.058182</td>\n",
       "      <td>0.004851</td>\n",
       "      <td>-0.032569</td>\n",
       "      <td>-0.083745</td>\n",
       "      <td>0.110139</td>\n",
       "      <td>-0.057365</td>\n",
       "      <td>-0.144832</td>\n",
       "      <td>-0.046770</td>\n",
       "      <td>-0.083594</td>\n",
       "      <td>0.054301</td>\n",
       "      <td>0.046492</td>\n",
       "      <td>-0.195701</td>\n",
       "      <td>-0.234877</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>lead_time</th>\n",
       "      <td>0.292876</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.040334</td>\n",
       "      <td>0.127046</td>\n",
       "      <td>0.002306</td>\n",
       "      <td>0.085985</td>\n",
       "      <td>0.166892</td>\n",
       "      <td>0.117575</td>\n",
       "      <td>-0.037878</td>\n",
       "      <td>-0.021003</td>\n",
       "      <td>-0.123209</td>\n",
       "      <td>0.086025</td>\n",
       "      <td>-0.073599</td>\n",
       "      <td>0.002230</td>\n",
       "      <td>-0.013114</td>\n",
       "      <td>-0.085854</td>\n",
       "      <td>0.170008</td>\n",
       "      <td>-0.065018</td>\n",
       "      <td>-0.116624</td>\n",
       "      <td>-0.095949</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>arrival_date_year</th>\n",
       "      <td>0.016622</td>\n",
       "      <td>0.040334</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.540373</td>\n",
       "      <td>-0.000121</td>\n",
       "      <td>0.021694</td>\n",
       "      <td>0.031203</td>\n",
       "      <td>0.030266</td>\n",
       "      <td>0.054710</td>\n",
       "      <td>-0.013192</td>\n",
       "      <td>0.010281</td>\n",
       "      <td>-0.119905</td>\n",
       "      <td>0.029234</td>\n",
       "      <td>0.031416</td>\n",
       "      <td>0.056438</td>\n",
       "      <td>0.033682</td>\n",
       "      <td>-0.056348</td>\n",
       "      <td>0.198429</td>\n",
       "      <td>-0.013812</td>\n",
       "      <td>0.108610</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>arrival_date_week_number</th>\n",
       "      <td>0.008315</td>\n",
       "      <td>0.127046</td>\n",
       "      <td>-0.540373</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.066572</td>\n",
       "      <td>0.018629</td>\n",
       "      <td>0.016047</td>\n",
       "      <td>0.026567</td>\n",
       "      <td>0.005556</td>\n",
       "      <td>0.010417</td>\n",
       "      <td>-0.031125</td>\n",
       "      <td>0.035493</td>\n",
       "      <td>-0.021009</td>\n",
       "      <td>0.006311</td>\n",
       "      <td>-0.018225</td>\n",
       "      <td>-0.032912</td>\n",
       "      <td>0.022677</td>\n",
       "      <td>0.076281</td>\n",
       "      <td>0.001980</td>\n",
       "      <td>0.026202</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>arrival_date_day_of_month</th>\n",
       "      <td>-0.005948</td>\n",
       "      <td>0.002306</td>\n",
       "      <td>-0.000121</td>\n",
       "      <td>0.066572</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.016225</td>\n",
       "      <td>-0.028362</td>\n",
       "      <td>-0.001754</td>\n",
       "      <td>0.014550</td>\n",
       "      <td>-0.000235</td>\n",
       "      <td>-0.006471</td>\n",
       "      <td>-0.027027</td>\n",
       "      <td>-0.000306</td>\n",
       "      <td>0.011266</td>\n",
       "      <td>0.000159</td>\n",
       "      <td>0.003667</td>\n",
       "      <td>0.022532</td>\n",
       "      <td>0.030291</td>\n",
       "      <td>0.008569</td>\n",
       "      <td>0.003026</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>stays_in_weekend_nights</th>\n",
       "      <td>-0.001323</td>\n",
       "      <td>0.085985</td>\n",
       "      <td>0.021694</td>\n",
       "      <td>0.018629</td>\n",
       "      <td>-0.016225</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.494175</td>\n",
       "      <td>0.094759</td>\n",
       "      <td>0.046135</td>\n",
       "      <td>0.018607</td>\n",
       "      <td>-0.086009</td>\n",
       "      <td>-0.012769</td>\n",
       "      <td>-0.042859</td>\n",
       "      <td>0.050191</td>\n",
       "      <td>0.162411</td>\n",
       "      <td>-0.080783</td>\n",
       "      <td>-0.054399</td>\n",
       "      <td>0.050670</td>\n",
       "      <td>-0.018520</td>\n",
       "      <td>0.073124</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>stays_in_week_nights</th>\n",
       "      <td>0.025542</td>\n",
       "      <td>0.166892</td>\n",
       "      <td>0.031203</td>\n",
       "      <td>0.016047</td>\n",
       "      <td>-0.028362</td>\n",
       "      <td>0.494175</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.096214</td>\n",
       "      <td>0.044652</td>\n",
       "      <td>0.020373</td>\n",
       "      <td>-0.095302</td>\n",
       "      <td>-0.013976</td>\n",
       "      <td>-0.048873</td>\n",
       "      <td>0.080018</td>\n",
       "      <td>0.196777</td>\n",
       "      <td>-0.044437</td>\n",
       "      <td>-0.002026</td>\n",
       "      <td>0.066847</td>\n",
       "      <td>-0.024933</td>\n",
       "      <td>0.068738</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>adults</th>\n",
       "      <td>0.058182</td>\n",
       "      <td>0.117575</td>\n",
       "      <td>0.030266</td>\n",
       "      <td>0.026567</td>\n",
       "      <td>-0.001754</td>\n",
       "      <td>0.094759</td>\n",
       "      <td>0.096214</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.029409</td>\n",
       "      <td>0.017890</td>\n",
       "      <td>-0.140973</td>\n",
       "      <td>-0.007070</td>\n",
       "      <td>-0.108856</td>\n",
       "      <td>-0.041472</td>\n",
       "      <td>0.023370</td>\n",
       "      <td>-0.166182</td>\n",
       "      <td>-0.008365</td>\n",
       "      <td>0.224253</td>\n",
       "      <td>0.014438</td>\n",
       "      <td>0.123353</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>children</th>\n",
       "      <td>0.004851</td>\n",
       "      <td>-0.037878</td>\n",
       "      <td>0.054710</td>\n",
       "      <td>0.005556</td>\n",
       "      <td>0.014550</td>\n",
       "      <td>0.046135</td>\n",
       "      <td>0.044652</td>\n",
       "      <td>0.029409</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.023999</td>\n",
       "      <td>-0.032475</td>\n",
       "      <td>-0.024755</td>\n",
       "      <td>-0.021078</td>\n",
       "      <td>0.051000</td>\n",
       "      <td>0.050461</td>\n",
       "      <td>-0.042554</td>\n",
       "      <td>-0.033293</td>\n",
       "      <td>0.325057</td>\n",
       "      <td>0.056247</td>\n",
       "      <td>0.081747</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>babies</th>\n",
       "      <td>-0.032569</td>\n",
       "      <td>-0.021003</td>\n",
       "      <td>-0.013192</td>\n",
       "      <td>0.010417</td>\n",
       "      <td>-0.000235</td>\n",
       "      <td>0.018607</td>\n",
       "      <td>0.020373</td>\n",
       "      <td>0.017890</td>\n",
       "      <td>0.023999</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.008813</td>\n",
       "      <td>-0.007509</td>\n",
       "      <td>-0.006552</td>\n",
       "      <td>0.085605</td>\n",
       "      <td>0.030235</td>\n",
       "      <td>-0.009426</td>\n",
       "      <td>-0.010627</td>\n",
       "      <td>0.029043</td>\n",
       "      <td>0.037389</td>\n",
       "      <td>0.097939</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>is_repeated_guest</th>\n",
       "      <td>-0.083745</td>\n",
       "      <td>-0.123209</td>\n",
       "      <td>0.010281</td>\n",
       "      <td>-0.031125</td>\n",
       "      <td>-0.006471</td>\n",
       "      <td>-0.086009</td>\n",
       "      <td>-0.095302</td>\n",
       "      <td>-0.140973</td>\n",
       "      <td>-0.032475</td>\n",
       "      <td>-0.008813</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.082740</td>\n",
       "      <td>0.420642</td>\n",
       "      <td>0.013044</td>\n",
       "      <td>-0.051584</td>\n",
       "      <td>0.161871</td>\n",
       "      <td>-0.022057</td>\n",
       "      <td>-0.130807</td>\n",
       "      <td>0.077928</td>\n",
       "      <td>0.012963</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>previous_cancellations</th>\n",
       "      <td>0.110139</td>\n",
       "      <td>0.086025</td>\n",
       "      <td>-0.119905</td>\n",
       "      <td>0.035493</td>\n",
       "      <td>-0.027027</td>\n",
       "      <td>-0.012769</td>\n",
       "      <td>-0.013976</td>\n",
       "      <td>-0.007070</td>\n",
       "      <td>-0.024755</td>\n",
       "      <td>-0.007509</td>\n",
       "      <td>0.082740</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.152570</td>\n",
       "      <td>-0.027261</td>\n",
       "      <td>-0.018251</td>\n",
       "      <td>-0.001110</td>\n",
       "      <td>0.005941</td>\n",
       "      <td>-0.065974</td>\n",
       "      <td>-0.018540</td>\n",
       "      <td>-0.048488</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>previous_bookings_not_canceled</th>\n",
       "      <td>-0.057365</td>\n",
       "      <td>-0.073599</td>\n",
       "      <td>0.029234</td>\n",
       "      <td>-0.021009</td>\n",
       "      <td>-0.000306</td>\n",
       "      <td>-0.042859</td>\n",
       "      <td>-0.048873</td>\n",
       "      <td>-0.108856</td>\n",
       "      <td>-0.021078</td>\n",
       "      <td>-0.006552</td>\n",
       "      <td>0.420642</td>\n",
       "      <td>0.152570</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.011963</td>\n",
       "      <td>-0.046348</td>\n",
       "      <td>0.111220</td>\n",
       "      <td>-0.009416</td>\n",
       "      <td>-0.072335</td>\n",
       "      <td>0.047506</td>\n",
       "      <td>0.037775</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>booking_changes</th>\n",
       "      <td>-0.144832</td>\n",
       "      <td>0.002230</td>\n",
       "      <td>0.031416</td>\n",
       "      <td>0.006311</td>\n",
       "      <td>0.011266</td>\n",
       "      <td>0.050191</td>\n",
       "      <td>0.080018</td>\n",
       "      <td>-0.041472</td>\n",
       "      <td>0.051000</td>\n",
       "      <td>0.085605</td>\n",
       "      <td>0.013044</td>\n",
       "      <td>-0.027261</td>\n",
       "      <td>0.011963</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.038555</td>\n",
       "      <td>0.089768</td>\n",
       "      <td>-0.011916</td>\n",
       "      <td>0.026601</td>\n",
       "      <td>0.067490</td>\n",
       "      <td>0.055003</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>agent</th>\n",
       "      <td>-0.046770</td>\n",
       "      <td>-0.013114</td>\n",
       "      <td>0.056438</td>\n",
       "      <td>-0.018225</td>\n",
       "      <td>0.000159</td>\n",
       "      <td>0.162411</td>\n",
       "      <td>0.196777</td>\n",
       "      <td>0.023370</td>\n",
       "      <td>0.050461</td>\n",
       "      <td>0.030235</td>\n",
       "      <td>-0.051584</td>\n",
       "      <td>-0.018251</td>\n",
       "      <td>-0.046348</td>\n",
       "      <td>0.038555</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.121333</td>\n",
       "      <td>-0.041182</td>\n",
       "      <td>0.015711</td>\n",
       "      <td>0.119282</td>\n",
       "      <td>0.060783</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>company</th>\n",
       "      <td>-0.083594</td>\n",
       "      <td>-0.085854</td>\n",
       "      <td>0.033682</td>\n",
       "      <td>-0.032912</td>\n",
       "      <td>0.003667</td>\n",
       "      <td>-0.080783</td>\n",
       "      <td>-0.044437</td>\n",
       "      <td>-0.166182</td>\n",
       "      <td>-0.042554</td>\n",
       "      <td>-0.009426</td>\n",
       "      <td>0.161871</td>\n",
       "      <td>-0.001110</td>\n",
       "      <td>0.111220</td>\n",
       "      <td>0.089768</td>\n",
       "      <td>-0.121333</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.022944</td>\n",
       "      <td>-0.127641</td>\n",
       "      <td>0.038638</td>\n",
       "      <td>-0.090790</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>days_in_waiting_list</th>\n",
       "      <td>0.054301</td>\n",
       "      <td>0.170008</td>\n",
       "      <td>-0.056348</td>\n",
       "      <td>0.022677</td>\n",
       "      <td>0.022532</td>\n",
       "      <td>-0.054399</td>\n",
       "      <td>-0.002026</td>\n",
       "      <td>-0.008365</td>\n",
       "      <td>-0.033293</td>\n",
       "      <td>-0.010627</td>\n",
       "      <td>-0.022057</td>\n",
       "      <td>0.005941</td>\n",
       "      <td>-0.009416</td>\n",
       "      <td>-0.011916</td>\n",
       "      <td>-0.041182</td>\n",
       "      <td>-0.022944</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.040859</td>\n",
       "      <td>-0.030601</td>\n",
       "      <td>-0.082755</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>adr</th>\n",
       "      <td>0.046492</td>\n",
       "      <td>-0.065018</td>\n",
       "      <td>0.198429</td>\n",
       "      <td>0.076281</td>\n",
       "      <td>0.030291</td>\n",
       "      <td>0.050670</td>\n",
       "      <td>0.066847</td>\n",
       "      <td>0.224253</td>\n",
       "      <td>0.325057</td>\n",
       "      <td>0.029043</td>\n",
       "      <td>-0.130807</td>\n",
       "      <td>-0.065974</td>\n",
       "      <td>-0.072335</td>\n",
       "      <td>0.026601</td>\n",
       "      <td>0.015711</td>\n",
       "      <td>-0.127641</td>\n",
       "      <td>-0.040859</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.056510</td>\n",
       "      <td>0.172308</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>required_car_parking_spaces</th>\n",
       "      <td>-0.195701</td>\n",
       "      <td>-0.116624</td>\n",
       "      <td>-0.013812</td>\n",
       "      <td>0.001980</td>\n",
       "      <td>0.008569</td>\n",
       "      <td>-0.018520</td>\n",
       "      <td>-0.024933</td>\n",
       "      <td>0.014438</td>\n",
       "      <td>0.056247</td>\n",
       "      <td>0.037389</td>\n",
       "      <td>0.077928</td>\n",
       "      <td>-0.018540</td>\n",
       "      <td>0.047506</td>\n",
       "      <td>0.067490</td>\n",
       "      <td>0.119282</td>\n",
       "      <td>0.038638</td>\n",
       "      <td>-0.030601</td>\n",
       "      <td>0.056510</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.082718</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>total_of_special_requests</th>\n",
       "      <td>-0.234877</td>\n",
       "      <td>-0.095949</td>\n",
       "      <td>0.108610</td>\n",
       "      <td>0.026202</td>\n",
       "      <td>0.003026</td>\n",
       "      <td>0.073124</td>\n",
       "      <td>0.068738</td>\n",
       "      <td>0.123353</td>\n",
       "      <td>0.081747</td>\n",
       "      <td>0.097939</td>\n",
       "      <td>0.012963</td>\n",
       "      <td>-0.048488</td>\n",
       "      <td>0.037775</td>\n",
       "      <td>0.055003</td>\n",
       "      <td>0.060783</td>\n",
       "      <td>-0.090790</td>\n",
       "      <td>-0.082755</td>\n",
       "      <td>0.172308</td>\n",
       "      <td>0.082718</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                is_canceled  lead_time  arrival_date_year  \\\n",
       "is_canceled                        1.000000   0.292876           0.016622   \n",
       "lead_time                          0.292876   1.000000           0.040334   \n",
       "arrival_date_year                  0.016622   0.040334           1.000000   \n",
       "arrival_date_week_number           0.008315   0.127046          -0.540373   \n",
       "arrival_date_day_of_month         -0.005948   0.002306          -0.000121   \n",
       "stays_in_weekend_nights           -0.001323   0.085985           0.021694   \n",
       "stays_in_week_nights               0.025542   0.166892           0.031203   \n",
       "adults                             0.058182   0.117575           0.030266   \n",
       "children                           0.004851  -0.037878           0.054710   \n",
       "babies                            -0.032569  -0.021003          -0.013192   \n",
       "is_repeated_guest                 -0.083745  -0.123209           0.010281   \n",
       "previous_cancellations             0.110139   0.086025          -0.119905   \n",
       "previous_bookings_not_canceled    -0.057365  -0.073599           0.029234   \n",
       "booking_changes                   -0.144832   0.002230           0.031416   \n",
       "agent                             -0.046770  -0.013114           0.056438   \n",
       "company                           -0.083594  -0.085854           0.033682   \n",
       "days_in_waiting_list               0.054301   0.170008          -0.056348   \n",
       "adr                                0.046492  -0.065018           0.198429   \n",
       "required_car_parking_spaces       -0.195701  -0.116624          -0.013812   \n",
       "total_of_special_requests         -0.234877  -0.095949           0.108610   \n",
       "\n",
       "                                arrival_date_week_number  \\\n",
       "is_canceled                                     0.008315   \n",
       "lead_time                                       0.127046   \n",
       "arrival_date_year                              -0.540373   \n",
       "arrival_date_week_number                        1.000000   \n",
       "arrival_date_day_of_month                       0.066572   \n",
       "stays_in_weekend_nights                         0.018629   \n",
       "stays_in_week_nights                            0.016047   \n",
       "adults                                          0.026567   \n",
       "children                                        0.005556   \n",
       "babies                                          0.010417   \n",
       "is_repeated_guest                              -0.031125   \n",
       "previous_cancellations                          0.035493   \n",
       "previous_bookings_not_canceled                 -0.021009   \n",
       "booking_changes                                 0.006311   \n",
       "agent                                          -0.018225   \n",
       "company                                        -0.032912   \n",
       "days_in_waiting_list                            0.022677   \n",
       "adr                                             0.076281   \n",
       "required_car_parking_spaces                     0.001980   \n",
       "total_of_special_requests                       0.026202   \n",
       "\n",
       "                                arrival_date_day_of_month  \\\n",
       "is_canceled                                     -0.005948   \n",
       "lead_time                                        0.002306   \n",
       "arrival_date_year                               -0.000121   \n",
       "arrival_date_week_number                         0.066572   \n",
       "arrival_date_day_of_month                        1.000000   \n",
       "stays_in_weekend_nights                         -0.016225   \n",
       "stays_in_week_nights                            -0.028362   \n",
       "adults                                          -0.001754   \n",
       "children                                         0.014550   \n",
       "babies                                          -0.000235   \n",
       "is_repeated_guest                               -0.006471   \n",
       "previous_cancellations                          -0.027027   \n",
       "previous_bookings_not_canceled                  -0.000306   \n",
       "booking_changes                                  0.011266   \n",
       "agent                                            0.000159   \n",
       "company                                          0.003667   \n",
       "days_in_waiting_list                             0.022532   \n",
       "adr                                              0.030291   \n",
       "required_car_parking_spaces                      0.008569   \n",
       "total_of_special_requests                        0.003026   \n",
       "\n",
       "                                stays_in_weekend_nights  stays_in_week_nights  \\\n",
       "is_canceled                                   -0.001323              0.025542   \n",
       "lead_time                                      0.085985              0.166892   \n",
       "arrival_date_year                              0.021694              0.031203   \n",
       "arrival_date_week_number                       0.018629              0.016047   \n",
       "arrival_date_day_of_month                     -0.016225             -0.028362   \n",
       "stays_in_weekend_nights                        1.000000              0.494175   \n",
       "stays_in_week_nights                           0.494175              1.000000   \n",
       "adults                                         0.094759              0.096214   \n",
       "children                                       0.046135              0.044652   \n",
       "babies                                         0.018607              0.020373   \n",
       "is_repeated_guest                             -0.086009             -0.095302   \n",
       "previous_cancellations                        -0.012769             -0.013976   \n",
       "previous_bookings_not_canceled                -0.042859             -0.048873   \n",
       "booking_changes                                0.050191              0.080018   \n",
       "agent                                          0.162411              0.196777   \n",
       "company                                       -0.080783             -0.044437   \n",
       "days_in_waiting_list                          -0.054399             -0.002026   \n",
       "adr                                            0.050670              0.066847   \n",
       "required_car_parking_spaces                   -0.018520             -0.024933   \n",
       "total_of_special_requests                      0.073124              0.068738   \n",
       "\n",
       "                                  adults  children    babies  \\\n",
       "is_canceled                     0.058182  0.004851 -0.032569   \n",
       "lead_time                       0.117575 -0.037878 -0.021003   \n",
       "arrival_date_year               0.030266  0.054710 -0.013192   \n",
       "arrival_date_week_number        0.026567  0.005556  0.010417   \n",
       "arrival_date_day_of_month      -0.001754  0.014550 -0.000235   \n",
       "stays_in_weekend_nights         0.094759  0.046135  0.018607   \n",
       "stays_in_week_nights            0.096214  0.044652  0.020373   \n",
       "adults                          1.000000  0.029409  0.017890   \n",
       "children                        0.029409  1.000000  0.023999   \n",
       "babies                          0.017890  0.023999  1.000000   \n",
       "is_repeated_guest              -0.140973 -0.032475 -0.008813   \n",
       "previous_cancellations         -0.007070 -0.024755 -0.007509   \n",
       "previous_bookings_not_canceled -0.108856 -0.021078 -0.006552   \n",
       "booking_changes                -0.041472  0.051000  0.085605   \n",
       "agent                           0.023370  0.050461  0.030235   \n",
       "company                        -0.166182 -0.042554 -0.009426   \n",
       "days_in_waiting_list           -0.008365 -0.033293 -0.010627   \n",
       "adr                             0.224253  0.325057  0.029043   \n",
       "required_car_parking_spaces     0.014438  0.056247  0.037389   \n",
       "total_of_special_requests       0.123353  0.081747  0.097939   \n",
       "\n",
       "                                is_repeated_guest  previous_cancellations  \\\n",
       "is_canceled                             -0.083745                0.110139   \n",
       "lead_time                               -0.123209                0.086025   \n",
       "arrival_date_year                        0.010281               -0.119905   \n",
       "arrival_date_week_number                -0.031125                0.035493   \n",
       "arrival_date_day_of_month               -0.006471               -0.027027   \n",
       "stays_in_weekend_nights                 -0.086009               -0.012769   \n",
       "stays_in_week_nights                    -0.095302               -0.013976   \n",
       "adults                                  -0.140973               -0.007070   \n",
       "children                                -0.032475               -0.024755   \n",
       "babies                                  -0.008813               -0.007509   \n",
       "is_repeated_guest                        1.000000                0.082740   \n",
       "previous_cancellations                   0.082740                1.000000   \n",
       "previous_bookings_not_canceled           0.420642                0.152570   \n",
       "booking_changes                          0.013044               -0.027261   \n",
       "agent                                   -0.051584               -0.018251   \n",
       "company                                  0.161871               -0.001110   \n",
       "days_in_waiting_list                    -0.022057                0.005941   \n",
       "adr                                     -0.130807               -0.065974   \n",
       "required_car_parking_spaces              0.077928               -0.018540   \n",
       "total_of_special_requests                0.012963               -0.048488   \n",
       "\n",
       "                                previous_bookings_not_canceled  \\\n",
       "is_canceled                                          -0.057365   \n",
       "lead_time                                            -0.073599   \n",
       "arrival_date_year                                     0.029234   \n",
       "arrival_date_week_number                             -0.021009   \n",
       "arrival_date_day_of_month                            -0.000306   \n",
       "stays_in_weekend_nights                              -0.042859   \n",
       "stays_in_week_nights                                 -0.048873   \n",
       "adults                                               -0.108856   \n",
       "children                                             -0.021078   \n",
       "babies                                               -0.006552   \n",
       "is_repeated_guest                                     0.420642   \n",
       "previous_cancellations                                0.152570   \n",
       "previous_bookings_not_canceled                        1.000000   \n",
       "booking_changes                                       0.011963   \n",
       "agent                                                -0.046348   \n",
       "company                                               0.111220   \n",
       "days_in_waiting_list                                 -0.009416   \n",
       "adr                                                  -0.072335   \n",
       "required_car_parking_spaces                           0.047506   \n",
       "total_of_special_requests                             0.037775   \n",
       "\n",
       "                                booking_changes     agent   company  \\\n",
       "is_canceled                           -0.144832 -0.046770 -0.083594   \n",
       "lead_time                              0.002230 -0.013114 -0.085854   \n",
       "arrival_date_year                      0.031416  0.056438  0.033682   \n",
       "arrival_date_week_number               0.006311 -0.018225 -0.032912   \n",
       "arrival_date_day_of_month              0.011266  0.000159  0.003667   \n",
       "stays_in_weekend_nights                0.050191  0.162411 -0.080783   \n",
       "stays_in_week_nights                   0.080018  0.196777 -0.044437   \n",
       "adults                                -0.041472  0.023370 -0.166182   \n",
       "children                               0.051000  0.050461 -0.042554   \n",
       "babies                                 0.085605  0.030235 -0.009426   \n",
       "is_repeated_guest                      0.013044 -0.051584  0.161871   \n",
       "previous_cancellations                -0.027261 -0.018251 -0.001110   \n",
       "previous_bookings_not_canceled         0.011963 -0.046348  0.111220   \n",
       "booking_changes                        1.000000  0.038555  0.089768   \n",
       "agent                                  0.038555  1.000000 -0.121333   \n",
       "company                                0.089768 -0.121333  1.000000   \n",
       "days_in_waiting_list                  -0.011916 -0.041182 -0.022944   \n",
       "adr                                    0.026601  0.015711 -0.127641   \n",
       "required_car_parking_spaces            0.067490  0.119282  0.038638   \n",
       "total_of_special_requests              0.055003  0.060783 -0.090790   \n",
       "\n",
       "                                days_in_waiting_list       adr  \\\n",
       "is_canceled                                 0.054301  0.046492   \n",
       "lead_time                                   0.170008 -0.065018   \n",
       "arrival_date_year                          -0.056348  0.198429   \n",
       "arrival_date_week_number                    0.022677  0.076281   \n",
       "arrival_date_day_of_month                   0.022532  0.030291   \n",
       "stays_in_weekend_nights                    -0.054399  0.050670   \n",
       "stays_in_week_nights                       -0.002026  0.066847   \n",
       "adults                                     -0.008365  0.224253   \n",
       "children                                   -0.033293  0.325057   \n",
       "babies                                     -0.010627  0.029043   \n",
       "is_repeated_guest                          -0.022057 -0.130807   \n",
       "previous_cancellations                      0.005941 -0.065974   \n",
       "previous_bookings_not_canceled             -0.009416 -0.072335   \n",
       "booking_changes                            -0.011916  0.026601   \n",
       "agent                                      -0.041182  0.015711   \n",
       "company                                    -0.022944 -0.127641   \n",
       "days_in_waiting_list                        1.000000 -0.040859   \n",
       "adr                                        -0.040859  1.000000   \n",
       "required_car_parking_spaces                -0.030601  0.056510   \n",
       "total_of_special_requests                  -0.082755  0.172308   \n",
       "\n",
       "                                required_car_parking_spaces  \\\n",
       "is_canceled                                       -0.195701   \n",
       "lead_time                                         -0.116624   \n",
       "arrival_date_year                                 -0.013812   \n",
       "arrival_date_week_number                           0.001980   \n",
       "arrival_date_day_of_month                          0.008569   \n",
       "stays_in_weekend_nights                           -0.018520   \n",
       "stays_in_week_nights                              -0.024933   \n",
       "adults                                             0.014438   \n",
       "children                                           0.056247   \n",
       "babies                                             0.037389   \n",
       "is_repeated_guest                                  0.077928   \n",
       "previous_cancellations                            -0.018540   \n",
       "previous_bookings_not_canceled                     0.047506   \n",
       "booking_changes                                    0.067490   \n",
       "agent                                              0.119282   \n",
       "company                                            0.038638   \n",
       "days_in_waiting_list                              -0.030601   \n",
       "adr                                                0.056510   \n",
       "required_car_parking_spaces                        1.000000   \n",
       "total_of_special_requests                          0.082718   \n",
       "\n",
       "                                total_of_special_requests  \n",
       "is_canceled                                     -0.234877  \n",
       "lead_time                                       -0.095949  \n",
       "arrival_date_year                                0.108610  \n",
       "arrival_date_week_number                         0.026202  \n",
       "arrival_date_day_of_month                        0.003026  \n",
       "stays_in_weekend_nights                          0.073124  \n",
       "stays_in_week_nights                             0.068738  \n",
       "adults                                           0.123353  \n",
       "children                                         0.081747  \n",
       "babies                                           0.097939  \n",
       "is_repeated_guest                                0.012963  \n",
       "previous_cancellations                          -0.048488  \n",
       "previous_bookings_not_canceled                   0.037775  \n",
       "booking_changes                                  0.055003  \n",
       "agent                                            0.060783  \n",
       "company                                         -0.090790  \n",
       "days_in_waiting_list                            -0.082755  \n",
       "adr                                              0.172308  \n",
       "required_car_parking_spaces                      0.082718  \n",
       "total_of_special_requests                        1.000000  "
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.corr()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "bf04c3b1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "is_canceled                       1.000000\n",
       "lead_time                         0.292876\n",
       "arrival_date_year                 0.016622\n",
       "arrival_date_week_number          0.008315\n",
       "arrival_date_day_of_month        -0.005948\n",
       "stays_in_weekend_nights          -0.001323\n",
       "stays_in_week_nights              0.025542\n",
       "adults                            0.058182\n",
       "children                          0.004851\n",
       "babies                           -0.032569\n",
       "is_repeated_guest                -0.083745\n",
       "previous_cancellations            0.110139\n",
       "previous_bookings_not_canceled   -0.057365\n",
       "booking_changes                  -0.144832\n",
       "agent                            -0.046770\n",
       "company                          -0.083594\n",
       "days_in_waiting_list              0.054301\n",
       "adr                               0.046492\n",
       "required_car_parking_spaces      -0.195701\n",
       "total_of_special_requests        -0.234877\n",
       "Name: is_canceled, dtype: float64"
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "co_relation=data.corr()['is_canceled']\n",
    "co_relation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "7dcbfdcc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "is_canceled                       1.000000\n",
       "lead_time                         0.292876\n",
       "total_of_special_requests         0.234877\n",
       "required_car_parking_spaces       0.195701\n",
       "booking_changes                   0.144832\n",
       "previous_cancellations            0.110139\n",
       "is_repeated_guest                 0.083745\n",
       "company                           0.083594\n",
       "adults                            0.058182\n",
       "previous_bookings_not_canceled    0.057365\n",
       "days_in_waiting_list              0.054301\n",
       "agent                             0.046770\n",
       "adr                               0.046492\n",
       "babies                            0.032569\n",
       "stays_in_week_nights              0.025542\n",
       "arrival_date_year                 0.016622\n",
       "arrival_date_week_number          0.008315\n",
       "arrival_date_day_of_month         0.005948\n",
       "children                          0.004851\n",
       "stays_in_weekend_nights           0.001323\n",
       "Name: is_canceled, dtype: float64"
      ]
     },
     "execution_count": 77,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "co_relation.abs().sort_values(ascending=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "964558e4",
   "metadata": {},
   "outputs": [],
   "source": [
    "list_not=data.groupby('is_canceled')['reservation_status'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "20f4a506",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['is_canceled',\n",
       " 'lead_time',\n",
       " 'arrival_date_year',\n",
       " 'arrival_date_week_number',\n",
       " 'arrival_date_day_of_month',\n",
       " 'stays_in_weekend_nights',\n",
       " 'stays_in_week_nights',\n",
       " 'adults',\n",
       " 'children',\n",
       " 'babies',\n",
       " 'is_repeated_guest',\n",
       " 'previous_cancellations',\n",
       " 'previous_bookings_not_canceled',\n",
       " 'booking_changes',\n",
       " 'agent',\n",
       " 'company',\n",
       " 'days_in_waiting_list',\n",
       " 'adr',\n",
       " 'required_car_parking_spaces',\n",
       " 'total_of_special_requests']"
      ]
     },
     "execution_count": 88,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cols=[]\n",
    "for col in data.columns:\n",
    "    if data[col].dtype!='O' and col not in list_not:\n",
    "        cols.append(col)\n",
    "cols"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "00ed5908",
   "metadata": {},
   "outputs": [],
   "source": [
    "num_features=[col for col in data.columns if data[col].dtype!='O' and col not in list_not]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "9fc8a619",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['is_canceled',\n",
       " 'lead_time',\n",
       " 'arrival_date_year',\n",
       " 'arrival_date_week_number',\n",
       " 'arrival_date_day_of_month',\n",
       " 'stays_in_weekend_nights',\n",
       " 'stays_in_week_nights',\n",
       " 'adults',\n",
       " 'children',\n",
       " 'babies',\n",
       " 'is_repeated_guest',\n",
       " 'previous_cancellations',\n",
       " 'previous_bookings_not_canceled',\n",
       " 'booking_changes',\n",
       " 'agent',\n",
       " 'company',\n",
       " 'days_in_waiting_list',\n",
       " 'adr',\n",
       " 'required_car_parking_spaces',\n",
       " 'total_of_special_requests']"
      ]
     },
     "execution_count": 90,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "num_features"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "id": "f2cd008f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['hotel', 'is_canceled', 'lead_time', 'arrival_date_year',\n",
       "       'arrival_date_month', 'arrival_date_week_number',\n",
       "       'arrival_date_day_of_month', 'stays_in_weekend_nights',\n",
       "       'stays_in_week_nights', 'adults', 'children', 'babies', 'meal',\n",
       "       'country', 'market_segment', 'distribution_channel',\n",
       "       'is_repeated_guest', 'previous_cancellations',\n",
       "       'previous_bookings_not_canceled', 'reserved_room_type',\n",
       "       'assigned_room_type', 'booking_changes', 'deposit_type', 'agent',\n",
       "       'company', 'days_in_waiting_list', 'customer_type', 'adr',\n",
       "       'required_car_parking_spaces', 'total_of_special_requests',\n",
       "       'reservation_status', 'reservation_status_date'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 91,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "6c7675ea",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['arrival_date_year',\n",
       " 'assigned_room_type',\n",
       " 'booking_changes',\n",
       " 'reservation_status',\n",
       " 'country',\n",
       " 'days_in_waiting_list']"
      ]
     },
     "execution_count": 92,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cat_not=['arrival_date_year','assigned_room_type','booking_changes', 'reservation_status','country','days_in_waiting_list']\n",
    "cat_not"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "id": "c2fce4ca",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['hotel',\n",
       " 'arrival_date_month',\n",
       " 'meal',\n",
       " 'market_segment',\n",
       " 'distribution_channel',\n",
       " 'reserved_room_type',\n",
       " 'deposit_type',\n",
       " 'customer_type',\n",
       " 'reservation_status_date']"
      ]
     },
     "execution_count": 102,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cat_features=[col for col in data.columns if data[col].dtype=='O'and col not in cat_not]\n",
    "cat_features"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "id": "83617c58",
   "metadata": {},
   "outputs": [],
   "source": [
    "data_cat=data[cat_features]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "id": "119da920",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>hotel</th>\n",
       "      <th>arrival_date_month</th>\n",
       "      <th>meal</th>\n",
       "      <th>market_segment</th>\n",
       "      <th>distribution_channel</th>\n",
       "      <th>reserved_room_type</th>\n",
       "      <th>deposit_type</th>\n",
       "      <th>customer_type</th>\n",
       "      <th>reservation_status_date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>July</td>\n",
       "      <td>BB</td>\n",
       "      <td>Direct</td>\n",
       "      <td>Direct</td>\n",
       "      <td>C</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>Transient</td>\n",
       "      <td>7/1/2015</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>July</td>\n",
       "      <td>BB</td>\n",
       "      <td>Direct</td>\n",
       "      <td>Direct</td>\n",
       "      <td>C</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>Transient</td>\n",
       "      <td>7/1/2015</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>July</td>\n",
       "      <td>BB</td>\n",
       "      <td>Direct</td>\n",
       "      <td>Direct</td>\n",
       "      <td>A</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>Transient</td>\n",
       "      <td>7/2/2015</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>July</td>\n",
       "      <td>BB</td>\n",
       "      <td>Corporate</td>\n",
       "      <td>Corporate</td>\n",
       "      <td>A</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>Transient</td>\n",
       "      <td>7/2/2015</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>July</td>\n",
       "      <td>BB</td>\n",
       "      <td>Online TA</td>\n",
       "      <td>TA/TO</td>\n",
       "      <td>A</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>Transient</td>\n",
       "      <td>7/3/2015</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          hotel arrival_date_month meal market_segment distribution_channel  \\\n",
       "0  Resort Hotel               July   BB         Direct               Direct   \n",
       "1  Resort Hotel               July   BB         Direct               Direct   \n",
       "2  Resort Hotel               July   BB         Direct               Direct   \n",
       "3  Resort Hotel               July   BB      Corporate            Corporate   \n",
       "4  Resort Hotel               July   BB      Online TA                TA/TO   \n",
       "\n",
       "  reserved_room_type deposit_type customer_type reservation_status_date  \n",
       "0                  C   No Deposit     Transient                7/1/2015  \n",
       "1                  C   No Deposit     Transient                7/1/2015  \n",
       "2                  A   No Deposit     Transient                7/2/2015  \n",
       "3                  A   No Deposit     Transient                7/2/2015  \n",
       "4                  A   No Deposit     Transient                7/3/2015  "
      ]
     },
     "execution_count": 104,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_cat.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "id": "a0a62bd6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "hotel                      object\n",
       "arrival_date_month         object\n",
       "meal                       object\n",
       "market_segment             object\n",
       "distribution_channel       object\n",
       "reserved_room_type         object\n",
       "deposit_type               object\n",
       "customer_type              object\n",
       "reservation_status_date    object\n",
       "dtype: object"
      ]
     },
     "execution_count": 105,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_cat.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "id": "155f2512",
   "metadata": {},
   "outputs": [],
   "source": [
    "import warnings\n",
    "from warnings import filterwarnings\n",
    "filterwarnings('ignore')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "id": "d5173b3d",
   "metadata": {},
   "outputs": [],
   "source": [
    "data_cat['reservation_status_date']=pd.to_datetime(data_cat['reservation_status_date'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "id": "c890a67d",
   "metadata": {},
   "outputs": [],
   "source": [
    "data_cat['year']=data_cat['reservation_status_date'].dt.year\n",
    "data_cat['month']=data_cat['reservation_status_date'].dt.month\n",
    "data_cat['day']=data_cat['reservation_status_date'].dt.day"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "id": "1da2b3eb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>hotel</th>\n",
       "      <th>arrival_date_month</th>\n",
       "      <th>meal</th>\n",
       "      <th>market_segment</th>\n",
       "      <th>distribution_channel</th>\n",
       "      <th>reserved_room_type</th>\n",
       "      <th>deposit_type</th>\n",
       "      <th>customer_type</th>\n",
       "      <th>reservation_status_date</th>\n",
       "      <th>year</th>\n",
       "      <th>month</th>\n",
       "      <th>day</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>July</td>\n",
       "      <td>BB</td>\n",
       "      <td>Direct</td>\n",
       "      <td>Direct</td>\n",
       "      <td>C</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>Transient</td>\n",
       "      <td>2015-07-01</td>\n",
       "      <td>2015</td>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>July</td>\n",
       "      <td>BB</td>\n",
       "      <td>Direct</td>\n",
       "      <td>Direct</td>\n",
       "      <td>C</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>Transient</td>\n",
       "      <td>2015-07-01</td>\n",
       "      <td>2015</td>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>July</td>\n",
       "      <td>BB</td>\n",
       "      <td>Direct</td>\n",
       "      <td>Direct</td>\n",
       "      <td>A</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>Transient</td>\n",
       "      <td>2015-07-02</td>\n",
       "      <td>2015</td>\n",
       "      <td>7</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>July</td>\n",
       "      <td>BB</td>\n",
       "      <td>Corporate</td>\n",
       "      <td>Corporate</td>\n",
       "      <td>A</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>Transient</td>\n",
       "      <td>2015-07-02</td>\n",
       "      <td>2015</td>\n",
       "      <td>7</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>July</td>\n",
       "      <td>BB</td>\n",
       "      <td>Online TA</td>\n",
       "      <td>TA/TO</td>\n",
       "      <td>A</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>Transient</td>\n",
       "      <td>2015-07-03</td>\n",
       "      <td>2015</td>\n",
       "      <td>7</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          hotel arrival_date_month meal market_segment distribution_channel  \\\n",
       "0  Resort Hotel               July   BB         Direct               Direct   \n",
       "1  Resort Hotel               July   BB         Direct               Direct   \n",
       "2  Resort Hotel               July   BB         Direct               Direct   \n",
       "3  Resort Hotel               July   BB      Corporate            Corporate   \n",
       "4  Resort Hotel               July   BB      Online TA                TA/TO   \n",
       "\n",
       "  reserved_room_type deposit_type customer_type reservation_status_date  year  \\\n",
       "0                  C   No Deposit     Transient              2015-07-01  2015   \n",
       "1                  C   No Deposit     Transient              2015-07-01  2015   \n",
       "2                  A   No Deposit     Transient              2015-07-02  2015   \n",
       "3                  A   No Deposit     Transient              2015-07-02  2015   \n",
       "4                  A   No Deposit     Transient              2015-07-03  2015   \n",
       "\n",
       "   month  day  \n",
       "0      7    1  \n",
       "1      7    1  \n",
       "2      7    2  \n",
       "3      7    2  \n",
       "4      7    3  "
      ]
     },
     "execution_count": 110,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_cat.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "id": "3bcc464b",
   "metadata": {},
   "outputs": [],
   "source": [
    "data_cat.drop('reservation_status_date',axis=1,inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "id": "9b41416f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>hotel</th>\n",
       "      <th>arrival_date_month</th>\n",
       "      <th>meal</th>\n",
       "      <th>market_segment</th>\n",
       "      <th>distribution_channel</th>\n",
       "      <th>reserved_room_type</th>\n",
       "      <th>deposit_type</th>\n",
       "      <th>customer_type</th>\n",
       "      <th>year</th>\n",
       "      <th>month</th>\n",
       "      <th>day</th>\n",
       "      <th>cancellation</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>July</td>\n",
       "      <td>BB</td>\n",
       "      <td>Direct</td>\n",
       "      <td>Direct</td>\n",
       "      <td>C</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>Transient</td>\n",
       "      <td>2015</td>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>July</td>\n",
       "      <td>BB</td>\n",
       "      <td>Direct</td>\n",
       "      <td>Direct</td>\n",
       "      <td>C</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>Transient</td>\n",
       "      <td>2015</td>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>July</td>\n",
       "      <td>BB</td>\n",
       "      <td>Direct</td>\n",
       "      <td>Direct</td>\n",
       "      <td>A</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>Transient</td>\n",
       "      <td>2015</td>\n",
       "      <td>7</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>July</td>\n",
       "      <td>BB</td>\n",
       "      <td>Corporate</td>\n",
       "      <td>Corporate</td>\n",
       "      <td>A</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>Transient</td>\n",
       "      <td>2015</td>\n",
       "      <td>7</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Resort Hotel</td>\n",
       "      <td>July</td>\n",
       "      <td>BB</td>\n",
       "      <td>Online TA</td>\n",
       "      <td>TA/TO</td>\n",
       "      <td>A</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>Transient</td>\n",
       "      <td>2015</td>\n",
       "      <td>7</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>119385</th>\n",
       "      <td>City Hotel</td>\n",
       "      <td>August</td>\n",
       "      <td>BB</td>\n",
       "      <td>Offline TA/TO</td>\n",
       "      <td>TA/TO</td>\n",
       "      <td>A</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>Transient</td>\n",
       "      <td>2017</td>\n",
       "      <td>9</td>\n",
       "      <td>6</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>119386</th>\n",
       "      <td>City Hotel</td>\n",
       "      <td>August</td>\n",
       "      <td>BB</td>\n",
       "      <td>Online TA</td>\n",
       "      <td>TA/TO</td>\n",
       "      <td>E</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>Transient</td>\n",
       "      <td>2017</td>\n",
       "      <td>9</td>\n",
       "      <td>7</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>119387</th>\n",
       "      <td>City Hotel</td>\n",
       "      <td>August</td>\n",
       "      <td>BB</td>\n",
       "      <td>Online TA</td>\n",
       "      <td>TA/TO</td>\n",
       "      <td>D</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>Transient</td>\n",
       "      <td>2017</td>\n",
       "      <td>9</td>\n",
       "      <td>7</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>119388</th>\n",
       "      <td>City Hotel</td>\n",
       "      <td>August</td>\n",
       "      <td>BB</td>\n",
       "      <td>Online TA</td>\n",
       "      <td>TA/TO</td>\n",
       "      <td>A</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>Transient</td>\n",
       "      <td>2017</td>\n",
       "      <td>9</td>\n",
       "      <td>7</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>119389</th>\n",
       "      <td>City Hotel</td>\n",
       "      <td>August</td>\n",
       "      <td>HB</td>\n",
       "      <td>Online TA</td>\n",
       "      <td>TA/TO</td>\n",
       "      <td>A</td>\n",
       "      <td>No Deposit</td>\n",
       "      <td>Transient</td>\n",
       "      <td>2017</td>\n",
       "      <td>9</td>\n",
       "      <td>7</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>119210 rows × 12 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "               hotel arrival_date_month meal market_segment  \\\n",
       "0       Resort Hotel               July   BB         Direct   \n",
       "1       Resort Hotel               July   BB         Direct   \n",
       "2       Resort Hotel               July   BB         Direct   \n",
       "3       Resort Hotel               July   BB      Corporate   \n",
       "4       Resort Hotel               July   BB      Online TA   \n",
       "...              ...                ...  ...            ...   \n",
       "119385    City Hotel             August   BB  Offline TA/TO   \n",
       "119386    City Hotel             August   BB      Online TA   \n",
       "119387    City Hotel             August   BB      Online TA   \n",
       "119388    City Hotel             August   BB      Online TA   \n",
       "119389    City Hotel             August   HB      Online TA   \n",
       "\n",
       "       distribution_channel reserved_room_type deposit_type customer_type  \\\n",
       "0                    Direct                  C   No Deposit     Transient   \n",
       "1                    Direct                  C   No Deposit     Transient   \n",
       "2                    Direct                  A   No Deposit     Transient   \n",
       "3                 Corporate                  A   No Deposit     Transient   \n",
       "4                     TA/TO                  A   No Deposit     Transient   \n",
       "...                     ...                ...          ...           ...   \n",
       "119385                TA/TO                  A   No Deposit     Transient   \n",
       "119386                TA/TO                  E   No Deposit     Transient   \n",
       "119387                TA/TO                  D   No Deposit     Transient   \n",
       "119388                TA/TO                  A   No Deposit     Transient   \n",
       "119389                TA/TO                  A   No Deposit     Transient   \n",
       "\n",
       "        year  month  day  cancellation  \n",
       "0       2015      7    1             0  \n",
       "1       2015      7    1             0  \n",
       "2       2015      7    2             0  \n",
       "3       2015      7    2             0  \n",
       "4       2015      7    3             0  \n",
       "...      ...    ...  ...           ...  \n",
       "119385  2017      9    6             0  \n",
       "119386  2017      9    7             0  \n",
       "119387  2017      9    7             0  \n",
       "119388  2017      9    7             0  \n",
       "119389  2017      9    7             0  \n",
       "\n",
       "[119210 rows x 12 columns]"
      ]
     },
     "execution_count": 115,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_cat['cancellation']=data['is_canceled']\n",
    "data_cat"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "id": "1d642975",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['Direct', 'Corporate', 'Online TA', 'Offline TA/TO',\n",
       "       'Complementary', 'Groups', 'Undefined', 'Aviation'], dtype=object)"
      ]
     },
     "execution_count": 116,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_cat['market_segment'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "id": "5e36d831",
   "metadata": {},
   "outputs": [],
   "source": [
    "cols=data_cat.columns[0:8]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "id": "7c4bb7e7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "hotel\n",
       "City Hotel      0.417859\n",
       "Resort Hotel    0.277674\n",
       "Name: cancellation, dtype: float64"
      ]
     },
     "execution_count": 126,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_cat.groupby(['hotel'])['cancellation'].mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "id": "181564f1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'City Hotel': 0.4178593534858457, 'Resort Hotel': 0.27767373336329815}\n",
      "{'April': 0.40783534934103627, 'August': 0.37782266791717767, 'December': 0.35034768456872317, 'February': 0.3344510680576254, 'January': 0.305016044587063, 'July': 0.37464409996836445, 'June': 0.41485954799158203, 'March': 0.32227682227682225, 'May': 0.3970288624787776, 'November': 0.31309998523113275, 'October': 0.38090966179241054, 'September': 0.3919047619047619}\n",
      "{'BB': 0.3741055553146277, 'FB': 0.5989974937343359, 'HB': 0.3446534790427445, 'SC': 0.3740638923120675, 'Undefined': 0.2446535500427716}\n",
      "{'Aviation': 0.22127659574468084, 'Complementary': 0.12225274725274725, 'Corporate': 0.18761832639151838, 'Direct': 0.15371165156572883, 'Groups': 0.6110858471022181, 'Offline TA/TO': 0.3433132081713671, 'Online TA': 0.3675897035881435, 'Undefined': 1.0}\n",
      "{'Corporate': 0.22056833558863329, 'Direct': 0.1748682499486688, 'GDS': 0.19170984455958548, 'TA/TO': 0.41059846547314577, 'Undefined': 0.8}\n",
      "{'A': 0.39156661581638, 'B': 0.3291479820627803, 'C': 0.3308270676691729, 'D': 0.31810834767193286, 'E': 0.2926829268292683, 'F': 0.304077401520387, 'G': 0.3647227533460803, 'H': 0.40765391014975044, 'L': 0.3333333333333333}\n",
      "{'No Deposit': 0.28401987344559215, 'Non Refund': 0.9936244601357374, 'Refundable': 0.2222222222222222}\n",
      "{'Contract': 0.3099214145383104, 'Group': 0.10104529616724739, 'Transient': 0.40786356117841654, 'Transient-Party': 0.25450414540816324}\n"
     ]
    }
   ],
   "source": [
    "for col in cols:\n",
    "    print(data_cat.groupby([col])['cancellation'].mean().to_dict())\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "id": "2572b8ac",
   "metadata": {},
   "outputs": [],
   "source": [
    "for col in cols:\n",
    "    dict=data_cat.groupby([col])['cancellation'].mean().to_dict()\n",
    "    data_cat[col]=data_cat[col].map(dict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "id": "6598ef78",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>hotel</th>\n",
       "      <th>arrival_date_month</th>\n",
       "      <th>meal</th>\n",
       "      <th>market_segment</th>\n",
       "      <th>distribution_channel</th>\n",
       "      <th>reserved_room_type</th>\n",
       "      <th>deposit_type</th>\n",
       "      <th>customer_type</th>\n",
       "      <th>year</th>\n",
       "      <th>month</th>\n",
       "      <th>day</th>\n",
       "      <th>cancellation</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.277674</td>\n",
       "      <td>0.374644</td>\n",
       "      <td>0.374106</td>\n",
       "      <td>0.153712</td>\n",
       "      <td>0.174868</td>\n",
       "      <td>0.330827</td>\n",
       "      <td>0.28402</td>\n",
       "      <td>0.407864</td>\n",
       "      <td>2015</td>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.277674</td>\n",
       "      <td>0.374644</td>\n",
       "      <td>0.374106</td>\n",
       "      <td>0.153712</td>\n",
       "      <td>0.174868</td>\n",
       "      <td>0.330827</td>\n",
       "      <td>0.28402</td>\n",
       "      <td>0.407864</td>\n",
       "      <td>2015</td>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0.277674</td>\n",
       "      <td>0.374644</td>\n",
       "      <td>0.374106</td>\n",
       "      <td>0.153712</td>\n",
       "      <td>0.174868</td>\n",
       "      <td>0.391567</td>\n",
       "      <td>0.28402</td>\n",
       "      <td>0.407864</td>\n",
       "      <td>2015</td>\n",
       "      <td>7</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0.277674</td>\n",
       "      <td>0.374644</td>\n",
       "      <td>0.374106</td>\n",
       "      <td>0.187618</td>\n",
       "      <td>0.220568</td>\n",
       "      <td>0.391567</td>\n",
       "      <td>0.28402</td>\n",
       "      <td>0.407864</td>\n",
       "      <td>2015</td>\n",
       "      <td>7</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0.277674</td>\n",
       "      <td>0.374644</td>\n",
       "      <td>0.374106</td>\n",
       "      <td>0.367590</td>\n",
       "      <td>0.410598</td>\n",
       "      <td>0.391567</td>\n",
       "      <td>0.28402</td>\n",
       "      <td>0.407864</td>\n",
       "      <td>2015</td>\n",
       "      <td>7</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      hotel  arrival_date_month      meal  market_segment  \\\n",
       "0  0.277674            0.374644  0.374106        0.153712   \n",
       "1  0.277674            0.374644  0.374106        0.153712   \n",
       "2  0.277674            0.374644  0.374106        0.153712   \n",
       "3  0.277674            0.374644  0.374106        0.187618   \n",
       "4  0.277674            0.374644  0.374106        0.367590   \n",
       "\n",
       "   distribution_channel  reserved_room_type  deposit_type  customer_type  \\\n",
       "0              0.174868            0.330827       0.28402       0.407864   \n",
       "1              0.174868            0.330827       0.28402       0.407864   \n",
       "2              0.174868            0.391567       0.28402       0.407864   \n",
       "3              0.220568            0.391567       0.28402       0.407864   \n",
       "4              0.410598            0.391567       0.28402       0.407864   \n",
       "\n",
       "   year  month  day  cancellation  \n",
       "0  2015      7    1             0  \n",
       "1  2015      7    1             0  \n",
       "2  2015      7    2             0  \n",
       "3  2015      7    2             0  \n",
       "4  2015      7    3             0  "
      ]
     },
     "execution_count": 130,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_cat.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "id": "62dc1998",
   "metadata": {},
   "outputs": [],
   "source": [
    "dataframe=pd.concat([data_cat,data[num_features]],axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 132,
   "id": "ba18a054",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>hotel</th>\n",
       "      <th>arrival_date_month</th>\n",
       "      <th>meal</th>\n",
       "      <th>market_segment</th>\n",
       "      <th>distribution_channel</th>\n",
       "      <th>reserved_room_type</th>\n",
       "      <th>deposit_type</th>\n",
       "      <th>customer_type</th>\n",
       "      <th>year</th>\n",
       "      <th>month</th>\n",
       "      <th>day</th>\n",
       "      <th>cancellation</th>\n",
       "      <th>is_canceled</th>\n",
       "      <th>lead_time</th>\n",
       "      <th>arrival_date_year</th>\n",
       "      <th>arrival_date_week_number</th>\n",
       "      <th>arrival_date_day_of_month</th>\n",
       "      <th>stays_in_weekend_nights</th>\n",
       "      <th>stays_in_week_nights</th>\n",
       "      <th>adults</th>\n",
       "      <th>children</th>\n",
       "      <th>babies</th>\n",
       "      <th>is_repeated_guest</th>\n",
       "      <th>previous_cancellations</th>\n",
       "      <th>previous_bookings_not_canceled</th>\n",
       "      <th>booking_changes</th>\n",
       "      <th>agent</th>\n",
       "      <th>company</th>\n",
       "      <th>days_in_waiting_list</th>\n",
       "      <th>adr</th>\n",
       "      <th>required_car_parking_spaces</th>\n",
       "      <th>total_of_special_requests</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.277674</td>\n",
       "      <td>0.374644</td>\n",
       "      <td>0.374106</td>\n",
       "      <td>0.153712</td>\n",
       "      <td>0.174868</td>\n",
       "      <td>0.330827</td>\n",
       "      <td>0.28402</td>\n",
       "      <td>0.407864</td>\n",
       "      <td>2015</td>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>342</td>\n",
       "      <td>2015</td>\n",
       "      <td>27</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.277674</td>\n",
       "      <td>0.374644</td>\n",
       "      <td>0.374106</td>\n",
       "      <td>0.153712</td>\n",
       "      <td>0.174868</td>\n",
       "      <td>0.330827</td>\n",
       "      <td>0.28402</td>\n",
       "      <td>0.407864</td>\n",
       "      <td>2015</td>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>737</td>\n",
       "      <td>2015</td>\n",
       "      <td>27</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0.277674</td>\n",
       "      <td>0.374644</td>\n",
       "      <td>0.374106</td>\n",
       "      <td>0.153712</td>\n",
       "      <td>0.174868</td>\n",
       "      <td>0.391567</td>\n",
       "      <td>0.28402</td>\n",
       "      <td>0.407864</td>\n",
       "      <td>2015</td>\n",
       "      <td>7</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>7</td>\n",
       "      <td>2015</td>\n",
       "      <td>27</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>75.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0.277674</td>\n",
       "      <td>0.374644</td>\n",
       "      <td>0.374106</td>\n",
       "      <td>0.187618</td>\n",
       "      <td>0.220568</td>\n",
       "      <td>0.391567</td>\n",
       "      <td>0.28402</td>\n",
       "      <td>0.407864</td>\n",
       "      <td>2015</td>\n",
       "      <td>7</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>13</td>\n",
       "      <td>2015</td>\n",
       "      <td>27</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>304.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>75.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0.277674</td>\n",
       "      <td>0.374644</td>\n",
       "      <td>0.374106</td>\n",
       "      <td>0.367590</td>\n",
       "      <td>0.410598</td>\n",
       "      <td>0.391567</td>\n",
       "      <td>0.28402</td>\n",
       "      <td>0.407864</td>\n",
       "      <td>2015</td>\n",
       "      <td>7</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>14</td>\n",
       "      <td>2015</td>\n",
       "      <td>27</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>240.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>98.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      hotel  arrival_date_month      meal  market_segment  \\\n",
       "0  0.277674            0.374644  0.374106        0.153712   \n",
       "1  0.277674            0.374644  0.374106        0.153712   \n",
       "2  0.277674            0.374644  0.374106        0.153712   \n",
       "3  0.277674            0.374644  0.374106        0.187618   \n",
       "4  0.277674            0.374644  0.374106        0.367590   \n",
       "\n",
       "   distribution_channel  reserved_room_type  deposit_type  customer_type  \\\n",
       "0              0.174868            0.330827       0.28402       0.407864   \n",
       "1              0.174868            0.330827       0.28402       0.407864   \n",
       "2              0.174868            0.391567       0.28402       0.407864   \n",
       "3              0.220568            0.391567       0.28402       0.407864   \n",
       "4              0.410598            0.391567       0.28402       0.407864   \n",
       "\n",
       "   year  month  day  cancellation  is_canceled  lead_time  arrival_date_year  \\\n",
       "0  2015      7    1             0            0        342               2015   \n",
       "1  2015      7    1             0            0        737               2015   \n",
       "2  2015      7    2             0            0          7               2015   \n",
       "3  2015      7    2             0            0         13               2015   \n",
       "4  2015      7    3             0            0         14               2015   \n",
       "\n",
       "   arrival_date_week_number  arrival_date_day_of_month  \\\n",
       "0                        27                          1   \n",
       "1                        27                          1   \n",
       "2                        27                          1   \n",
       "3                        27                          1   \n",
       "4                        27                          1   \n",
       "\n",
       "   stays_in_weekend_nights  stays_in_week_nights  adults  children  babies  \\\n",
       "0                        0                     0       2       0.0       0   \n",
       "1                        0                     0       2       0.0       0   \n",
       "2                        0                     1       1       0.0       0   \n",
       "3                        0                     1       1       0.0       0   \n",
       "4                        0                     2       2       0.0       0   \n",
       "\n",
       "   is_repeated_guest  previous_cancellations  previous_bookings_not_canceled  \\\n",
       "0                  0                       0                               0   \n",
       "1                  0                       0                               0   \n",
       "2                  0                       0                               0   \n",
       "3                  0                       0                               0   \n",
       "4                  0                       0                               0   \n",
       "\n",
       "   booking_changes  agent  company  days_in_waiting_list   adr  \\\n",
       "0                3    0.0      0.0                     0   0.0   \n",
       "1                4    0.0      0.0                     0   0.0   \n",
       "2                0    0.0      0.0                     0  75.0   \n",
       "3                0  304.0      0.0                     0  75.0   \n",
       "4                0  240.0      0.0                     0  98.0   \n",
       "\n",
       "   required_car_parking_spaces  total_of_special_requests  \n",
       "0                            0                          0  \n",
       "1                            0                          0  \n",
       "2                            0                          0  \n",
       "3                            0                          0  \n",
       "4                            0                          1  "
      ]
     },
     "execution_count": 132,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dataframe.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "id": "374fbaa1",
   "metadata": {},
   "outputs": [],
   "source": [
    "dataframe.drop('cancellation',axis=1,inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 134,
   "id": "0a957568",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(119210, 31)"
      ]
     },
     "execution_count": 134,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dataframe.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3a119e14",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
