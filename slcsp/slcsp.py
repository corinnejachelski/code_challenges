from csv import reader

def get_plans():
    with open('plans.csv') as plans:
        data = reader(plans)

        #create empty dicitonary to keep track of plan costs by rate area
        plans = {}

        for row in data:
            #check if metal_level is Silver
            if row[2] == "Silver":
                #create new data point for each row concatenating state and rate area (i.e. AL1)
                rate_area = f"{row[1]}{row[4]}"
                
                #create rate_area key if not existing, or add rate to list of values (i.e. 'WI3': ['369.4', '365.48'])
                plans[rate_area] = plans.get(rate_area, []) + [row[3]]

    return plans

def get_rate_area_by_zip():
    with open('zips.csv') as zips:
        data = reader(zips)

        #create empty dictionary to match zip codes and rate area (i.e. AL11: 36749)
        zip_ratearea = {}

        for row in data:
            rate_area = f"{row[1]}{row[4]}"
            zip_code = row[0]
            #create zip code key in dict if not existing, or add to list of values
            zip_ratearea[zip_code] = zip_ratearea.get(zip_code, []) + [rate_area]

    return zip_ratearea

def get_second_lowest_price():

    zip_ratearea = get_rate_area_by_zip()
    plans = get_plans()
    
    with open('slcsp.csv') as f:
        data = reader(f)

        next(data)
        print("zipcode,rate")

        for row in data:
            zip_code = row[0]
            second_lowest = row[1]

            #check if zip code in dictionary from zips.csv file
            if zip_code in zip_ratearea.keys():
                #get unique rate areas for zip code
                #ignore zip codes with more than 1 rate area
                if len(set(zip_ratearea[zip_code])) == 1:
                    #get rate area string from set
                    rate_area = set(zip_ratearea[zip_code]).pop()

                    if rate_area in plans.keys():
                        #sort the list of unique plan prices for the rate area
                        sorted_prices = sorted(set(plans[rate_area]))
                        
                        #make sure 2nd lowest price exists in data
                        if len(sorted_prices) >= 2:
                            #add second index item to row as second lowest price
                            second_lowest = '{:.2f}'.format(float(sorted_prices[1]))
                            
            print(f"{zip_code},{second_lowest}")



if __name__ == "__main__":
    get_second_lowest_price()