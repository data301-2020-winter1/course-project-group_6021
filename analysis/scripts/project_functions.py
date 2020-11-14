{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#These are the scripts for our project\n",
    "\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "from numpy import nan as NA\n",
    "\n",
    "def load_and_process(dataset):\n",
    "    df1 = (\n",
    "        pd.read_csv(dataset)\n",
    "        .dropna()\n",
    "        .rename(columns={'dteday':'Date','yr':'Year','cnt':'Total'})\n",
    "        \n",
    "    )\n",
    "    \n",
    "    df2 = (\n",
    "        df1.drop(columns=['instant'])\n",
    "            .assign(Ratio = df1['casual']/df1['registered'])\n",
    "    )\n",
    "    \n",
    "    return df2"
   ]
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
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
