class MultiPlayerSocket {
    constructor(playground) {
        this.playground = playground;

        this.ws = new WebSocket("wss://app5560.acapp.acwing.com.cn/wss/multiplayer/");

        this.start();
    }

    start() {
        
    }
}