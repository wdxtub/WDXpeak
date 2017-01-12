# Deck of Cards

出处

Design the data structures for a generic deck of cards. Explain how you would subclass the data structures to implement blackjack.

## Solution

Key point

+ What's the meaning of genetic

Assume the deck is a standard 52-card set.

Design may be like this:

## Code

```java
public enum Suit {
    Club(0), Diamond (1), Heart (2), Spade (3);
    private int value;
    private Suit(int v){ value = v;}
    public int getValue() { return value; }
    public static Suit getSuitFromValue(int value) {...}
}

public abstract class Card {
    private boolean available = true;
    
    protected int faceValue;
    protected Suit suit;
    
    public Card(int c, Suit s) {
        faceValue = c;
        suit = s;
    }
    
    public abstract int value();
    public Suit suit() { return suit; }
    
    // Checks if the card is available to be given out to someone
    public boolean isAvailable() { return available; }
    public void markUnavailable() { available = false; }
    public void markAvailable() { available = true; }
}

public class Deck <T extends Card> {
    private ArrayList<T> cards; // all cards, dealt or not
    private int dealtIndex = 0; // marks first undealt card
    
    public void setDeckOfCard(ArrayList<T> deckOfCards) {...}
    
    public void shuffle() {...}
    public int remainingCards(){
        return cards.size() - dealtIndex;
    }
    
    public T[] dealHand(int number) {...}
    public T dealCard() {...}
}

public class Hand <T extends Card> {
    protected ArrayList<T> cards = new ArrayList<T>();
    
    public int score() {
        int score = 0;
        for (T card : cards) {
            score += card.value();
        }
        return score;
    }
    
    public addCard(T card) {
        cards.add(card);
    }
}

``` 

