
```typescript
export class ExpirableCountDownTimer {
    private timer: NodeJS.Timer;
    private heartbeatTimer: NodeJS.Timeout;
    public isAlive: boolean = true;

    public constructor(public callback: () => void, public interval: number = 5000, public TTL: number = 30000) {
        this.timer = this.setupTimer();
        this.heartbeatTimer = this.heartbeat();
    }

    private setupTimer() {
        return setInterval(() => {
            this.callback();
        }, this.interval);
    }

    private resumeTimer() {
        clearInterval(this.timer);
        this.timer = this.setupTimer();
        this.isAlive = true;
    }

    private stopTimer() {
        clearInterval(this.timer);
        this.isAlive = false;
    }

    public revive() {
        if (this.isAlive === false) {
            this.resumeTimer();
            clearInterval(this.heartbeatTimer);
            this.heartbeatTimer = this.heartbeat();
        }
        this.isAlive = true;
    }

    private heartbeat() {
        return setInterval(() => {
            if (this.isAlive === false) {
                this.stopTimer();
                clearInterval(this.heartbeatTimer);
            }
            this.isAlive = false;
        }, this.TTL);
    }
}
```