class Address:
    def __init__(self, name, street, cap, city, region) -> None:
        self.name = name
        self.street = street
        self.cap = cap
        self.city = city
        self.region = region
        
    def __str__(self) -> str:
        return f"{self.name}\n{self.street}\n{self.cap} {self.city} ({self.region})"
    
    @staticmethod
    def get_recipient_address(number):
        addresses = [
            Address("SPRING GDS", "VIA BOVISASCA 18", "20026", "NOVATE MILANESE", "MI"),
           # Address("DVG AUTOMATION SPA", "Viale Gabriele Rossetti 2", "29016", "Cortemaggiore", "PC"),
           # Address("Gxo Logistics", "Via P.Le Georg Schaeffler 2", "13040", "Carisio", "VC"),
        ]
        
        # if 1 <= number <= len(addresses):
        #     return addresses[number]
        # else:
        return addresses[0]
    
    @staticmethod
    def get_sender_address(number):
        addresses = [
            Address("Marta Sciazzi", "Via Alberto 12", "25126", "Brescia", "BS"),
            Address("Luca Amendola", "Via Martiri 5", "24100", "Bergamo", "BG"),
            Address("Giorgia Rizzo", "Via Armando Diaz 32", "37100", "Verona", "VR"),
            Address("Marco Snuffi", "Via Tebaldo 23", "25064", "Gussago", "BS"),
            Address("Martina Fedi", "Via Mantova 12", "46100", "Mantova", "MN")
        ]
        
        if 1 <= number <= len(addresses):
            return addresses[number]
        else:
            return addresses[0]
        
    