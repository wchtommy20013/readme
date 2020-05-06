export class Car {
    public constructor(
        public make: string,
        public model: string,
        public color: string,
        public numDoors: number
    ) { }
}

export interface ICarBuilder {
    color: string;
    numDoors: number;

    getResult(): Car;
}

export class FerrariBuilder implements ICarBuilder {
    public color: string;
    public numDoors: number;

    public getResult(): Car {
        return this.numDoors == 2 ? new Car("Ferrari", "488 Spider", this.color, this.numDoors) : null;
    }
}

export class SportsCarBuildDirector {
    public constructor(private builder: ICarBuilder) { }

    public construct(): void {
        this.builder.color = "Red";
        this.builder.numDoors = 2;
    }
}


const builder = new FerrariBuilder();
const director = new SportsCarBuildDirector(builder);

director.construct();
const myRaceCar = builder.getResult();
