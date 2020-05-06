//Empty vocabulary of actual object
export interface IPerson {
    getName(): string;
}

export class Villager implements IPerson {
    public getName(): string {
        return "Village Person";
    }
}

export class CityPerson implements IPerson {
    public getName(): string {
        return "City Person";
    }
}

export enum PersonType {
    Rural,
    Urban
}

export class Factory {
    public getPerson(type: PersonType): IPerson {
        switch (type) {
            case PersonType.Rural:
                return new Villager();
            case PersonType.Urban:
                return new CityPerson();
            default:
                throw new Error('Not Implemented');
        }
    }
}

/**
 * In the above code you can see the creation of one interface called IPerson and two implementations called Villager and CityPerson. Based on the type passed into the Factory object, we are returning the original concrete object as the interface IPerson.
 * A factory method is just an addition to Factory class. It creates the object of the class through interfaces but on the other hand, it also lets the subclass decide which class is instantiated.
*/

export interface IProduct {
    getName(): string;
    setPrice(price: number);
}

export class Phone implements IProduct {
    private price: number;

    public getName(): string {
        return "Apple TouchPad";
    }

    public setPrice(price: number): string {
        this.price = price;
        return "success";
    }
}

/* Almost same as Factory, just an additional exposure to do something with the created method */
export abstract class ProductAbstractFactory {
    protected abstract makeProduct(): IProduct;

    public getObject(): IProduct // Implementation of Factory Method.
    {
        return this.makeProduct();
    }
}

export class PhoneConcreteFactory extends ProductAbstractFactory {
    protected makeProduct(): IProduct {
        const product: IProduct = new Phone();
        //Do something with the object after you get the object. 
        product.setPrice(20.30);
        return product;
    }
}
