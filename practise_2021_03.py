from Utils.tools import *

def main():
    
    data = data = get_input("202103", True)

    def get_column(matrix, i):
        column = [row[i] for row in matrix]
        return column

    diagnostic_report = clean_list_strings(data)

    matrix = []
    for d in diagnostic_report:
        matrix.append(list(d))



    def puzzle1(matrix):

        gamma_rate = ""
        epsilon_rate = ""

        for i in range(5):
            column = get_column(matrix, i)
            if column.count('0') > column.count('1'): 
                gamma_rate += "0"
                epsilon_rate += "1"

            else:
                gamma_rate += "1"
                epsilon_rate += "0"

        gamma_rate_decimal = int(gamma_rate, 2)
        epsilon_rate_decimal = int(epsilon_rate, 2)

        power_consumption = gamma_rate_decimal * epsilon_rate_decimal
        return power_consumption
        
    def get_oxygen_generator_rating(matrix):
        for i in range(5):
            column = get_column(matrix, i)
            if column.count('0') > column.count('1'): 
                matrix = [ row for row in matrix if row[i] == "0"]
            elif column.count('0') == column.count('1'):
                matrix = [ row for row in matrix if row[i] == "1"]
            else:
                matrix = [ row for row in matrix if row[i] == "1"]
            
            if len(matrix) == 1:
                break
        
        return ("".join(matrix[0]))   

    def get_co2_scrubber_rating(matrix):
        for i in range(5):
            column = get_column(matrix, i)
            if column.count('0') < column.count('1'): 
                matrix = [ row for row in matrix if row[i] == "0"]
            elif column.count('0') == column.count('1'):
                matrix = [ row for row in matrix if row[i] == "0"]
            else:
                matrix = [ row for row in matrix if row[i] == "1"]
            
            if len(matrix) == 1:
                break
        
        return ("".join(matrix[0])) 
    

    def puzzle2(matrix):

        oxygen_generator_rating = get_oxygen_generator_rating(matrix)
        co2_scrubber_rating = get_co2_scrubber_rating(matrix)

        oxygen_generator_rating_dec = int(oxygen_generator_rating, 2)
        co2_scrubber_rating_dec = int(co2_scrubber_rating, 2)

        life_support_rating = oxygen_generator_rating_dec * co2_scrubber_rating_dec
        return life_support_rating



    
    result_puzzle1 = puzzle1(matrix)
    result_puzzle2 = puzzle2(matrix)


    print(f"Answer for puzzle 1: {result_puzzle1}")
    print(f"Answer for puzzle 2: {result_puzzle2}")

if __name__ == "__main__":
    main()