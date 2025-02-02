class Solution:
    def Polulation(self, birth_rate, death_rate, current_population, days):
        population = current_population
        for i in range(days):
            births = birth_rate * population 
            deaths = death_rate * population 
            population += births - deaths
        return round(population)
if __name__ == "__main__":
    birth_rate = 0.5
    death_rate = 0.1
    days = 4
    current_population = 1000
    sol = Solution()
    print(sol.Polulation(birth_rate, death_rate, current_population, days))
