class AcGamePlayground{
    constructor(root){
        this.root = root;
        this.$playground = $(`<div class="ac_game_playground"></div>`);

        // this.hide();
        this.root.$ac_game.append(this.$playground);
        this.width = this.$playground.width();
        this.height = this.$playground.height();
        this.game_map = new GameMap(this); // 初始化地图
        this.players = []; // 存储所有角色

        // 添加自己的角色
        this.players.push(new Player(this, this.width/2, this.height/2,  this.height * 0.058, "white", this.height*0.15, true));

        for(let i = 0;i < 5;i ++ ){ // 添加5个AI对手
            this.players.push(new Player(this, this.width/2, this.height/2, this.height * 0.058, "blue", this.height * 0.15, false));
        }

        this.start();
    }

    start(){
    }

    show(){ // 打开playground页面
        this.$playground.show();
    }

    hide(){ // 关闭playground页面
        this.$playground.hide();
    }

}

