n=int(input())
cards=[int(card) for card in input().split()]
Sereja_points=0
Dima_points=0
for i in range(len(cards)):
    max_card = max(cards[0],cards[-1])
    if(i%2==0):
        Sereja_points+=max_card
    else:
        Dima_points+=max_card
    cards.remove(max_card)
print(Sereja_points,Dima_points)
    
    
    
    