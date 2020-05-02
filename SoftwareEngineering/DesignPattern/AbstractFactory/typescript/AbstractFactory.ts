export interface IButton {
    paint(): void;
}

export interface IGUIFactory {
    createButton(): IButton;
}

export class WinFactory implements IGUIFactory {
    public createButton(): IButton {
        return new WinButton();
    }
}

export class OSXFactory implements IGUIFactory {
    public createButton(): IButton {
        return new OSXButton();
    }
}

export class WinButton implements IButton {
    public paint(): void {
        //Render a button in a Windows style
    }
}

export class OSXButton implements IButton {
    public paint(): void {
        //Render a button in a Mac OS X style
    }
}

const render = (appearance: string): IGUIFactory => {
    let factory: IGUIFactory;
    switch (appearance) {
        case "Win":
            factory = new WinFactory();
            break;
        case "OSX":
            factory = new OSXFactory();
            break;
        default:
            throw new Error('Not Implemented');
    }
    return factory;
};

const appearance = 'Win';
const factory: IGUIFactory = render(appearance);

const button = factory.createButton();
button.paint();
