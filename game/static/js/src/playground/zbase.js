class AcGamePlayground{
    constructor(root){
        this.root = root;
        this.$playground = $(`<div class="ac_game_playfround></div>`);

        // this.hide();
        this.root.$ac_game.append(this.$playground);
        this.width = this.$playground.width();
        this.height = this.$playground.height();

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

