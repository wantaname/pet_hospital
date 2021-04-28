<template>
  <div class="container">
    <div id="canvas">
      <div class="text">
        <h3>注射室</h3>
        <p>包括静脉注射、皮下注射、肌肉注射、局部封闭注射的操作流程，常见问题的处理方法，输液泵、加热垫的使用方法，注射室的消毒流程。</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data(){
    return {

    }
  },

  mounted() {
    this.start()
  },
  methods:{
    start(){
      let texture = new THREE.TextureLoader().load("./texture/floor.jpg")

      console.log(texture)
      texture.wrapS = THREE.RepeatWrapping;
      texture.wrapT = THREE.RepeatWrapping;
      // uv两个方向纹理重复数量
      texture.repeat.set(50,25);

      let skyTexture = new THREE.TextureLoader().load("./texture/keji.jpg")


      // 1. 场景
      let scene = new THREE.Scene()
      // 场景设置
      // 背景颜色
      let sceneColor = new THREE.Color("rgb(168,190,230)")
      scene.background = skyTexture


      let ambient = new THREE.AmbientLight(new THREE.Color(0xffffff))
      scene.add(ambient)

      // 平面
      let plane = new THREE.BoxGeometry(400,3,200)
      let planeMaterial = new THREE.MeshBasicMaterial({
        // color: new THREE.Color("rgb(132,190,213)"),
        map:texture
      })
      let planeMesh = new THREE.Mesh(plane,planeMaterial)


      scene.add(planeMesh)


      // 传入：方向h/v、起始点、结束点数组.注意是XZ平面
      function createWall(dir,start,end,name){
        // 墙的高度
        let height = 40
        // 墙的厚度
        let depth = 3

        let wallArray = ["./texture/wall1.jpeg","./texture/wall2.jpeg","./texture/wall3.jpg","./texture/wall4.jpg",
          "./texture/wall5.jpg","./texture/wall6.jpg"]
        // 水平方向
        if(dir==="h"){
          let width = end[0]-start[0]

          let posX = (end[0]+start[0])/2
          let posZ = end[1]
          let posY = height/2
          let texture = null
          if(name==='outer'){
            texture = new THREE.TextureLoader().load("./texture/wall0.jpg")
          }
          else {
            let img = wallArray[Math.floor((Math.random()*wallArray.length))]
            texture = new THREE.TextureLoader().load(img)
          }
          texture.wrapS = THREE.RepeatWrapping;
          texture.wrapT = THREE.RepeatWrapping;
          // uv两个方向纹理重复数量
          texture.repeat.set(width/height,1);
          let wallMaterial = new THREE.MeshBasicMaterial({
            map:texture
          })

          let wallGeometry = new THREE.BoxGeometry(width,height,depth)
          let wallMesh = new THREE.Mesh(wallGeometry,wallMaterial)

          wallMesh.position.set(posX,posY,posZ)
          scene.add(wallMesh)
        }
        else {
          let width = end[1]-start[1]
          let posX = end[0]
          let posY = height /2
          let posZ = (end[1]+start[1])/2

          let texture = null
          if(name==="outer"){
            texture = new THREE.TextureLoader().load("./texture/wall0.jpg")
          }
          else {
            let img = wallArray[Math.floor((Math.random()*wallArray.length))]
            texture = new THREE.TextureLoader().load(img)
          }
          texture.wrapS = THREE.RepeatWrapping;
          texture.wrapT = THREE.RepeatWrapping;
          // uv两个方向纹理重复数量
          texture.repeat.set(width/height,1);
          let wallMaterial = new THREE.MeshBasicMaterial({
            map:texture
          })
          let wallGeometry = new THREE.BoxGeometry(depth,height,width)
          let wallMesh = new THREE.Mesh(wallGeometry,wallMaterial)

          wallMesh.position.set(posX,posY,posZ)
          scene.add(wallMesh)

        }
      }
      createWall("h",[-200,100],[200,100],name='outer')
      createWall("h",[-200,-100],[200,-100],name="outer")
      createWall("h",[-200,60],[-140,60])
      createWall("h",[-120,60],[-20,60])
      createWall("h",[20,60],[100,60])
      createWall("h",[120,60],[200,60])

      createWall("h",[-140,0],[-20,0])
      createWall("h",[20,0],[100,0])
      createWall("h",[-180,-50],[-40,-50])
      createWall("h",[-20,-50],[100,-50])


      createWall("v",[-200,-100],[-200,100],name="outer")
      createWall("v",[200,-100],[200,100],name="outer")

      createWall("v",[-140,-80],[-140,40])


      createWall("v",[120,-100],[120,-80])
      createWall("v",[120,-60],[120,60])
      createWall("v",[100,-50],[100,60])
      createWall("v",[-70,-100],[-70,-70])
      createWall("v",[50,-100],[50,-50])
      createWall("v",[-50,-50],[-50,-20])
      createWall("v",[50,-50],[50,-20])

      createWall("v",[-20,0],[-20,40])
      createWall("v",[20,0],[20,40])
      createWall("v",[-120,60],[-120,100])
      createWall("v",[0,60],[0,100])
      createWall("v",[100,60],[100,100])



      function createText(imgUrl,pos){
        let texture = new THREE.TextureLoader().load(imgUrl)
        let m = new THREE.SpriteMaterial({

          map:texture,

        })

        let textMesh = new THREE.Sprite(m)
        textMesh.scale.set(25,25,25)
        textMesh.position.set(pos[0],25,pos[1])

        scene.add(textMesh)
        return textMesh
      }

      let zhushe = createText("./text/zhushe.jpg",[-180,-80])
      let zhenshi = createText("./text/zhenshi.jpg",[-180,0])
      let mianyi = createText("./text/mianyi.jpg",[-170,80])
      let zhunbei = createText("./text/zhunbei.jpg",[-120,-80])
      let yaofang = createText("./text/yaofang.jpg",[-110,-30])
      let chuzhi = createText("./text/chuzhi.jpg",[-100,22])
      let huayan = createText("./text/huayan.jpg",[-90,80])
      let shoushu = createText("./text/shoushu.jpg",[-20,-80])
      let dangan = createText("./text/dangan.jpg",[70,-20])
      let bingli = createText("./text/bingli.jpg",[50,30])
      let yingxiang = createText("./text/yingxiang.jpg",[60,80])
      let zhuyuan = createText("./text/zhuyuan.jpg",[160,-40])
      let zhuanke= createText("./text/zhuanke.jpg",[150,80])


      //2.光照
      const light = new THREE.AmbientLight( 0xffffff ); // soft white light
      scene.add( light );


      // 3.相机： 视角、横纵比、近距离、远距离
      let camera = new THREE.PerspectiveCamera(60,8/5,0.1,2000)

      //
      // 相机设置
      camera.position.set(0,338,180)

      //
      // 4. 渲染器
      let renderer = new THREE.WebGLRenderer()
      document.querySelector("#canvas").appendChild(renderer.domElement)
      // 渲染的画布大小
      renderer.setSize(1000,618)



      var controls = new THREE.OrbitControls(camera,renderer.domElement);//创建控件对象

      // camera.lookAt(300,2,0)

      // 鼠标点击

      const raycaster = new THREE.Raycaster();
      const mouse = new THREE.Vector2();


      let textShow = document.querySelector(".text")

      let textTitle = textShow.querySelector("h3")
      let textContent  = textShow.querySelector("p")
      function show(title,text){
        console.log(111111111)
        textTitle.innerHTML = title
        textContent.innerHTML = text
        textShow.style["display"] = "block"

      }

      let canvas = document.querySelector("#canvas")

      function onClick( event ) {



        // 将鼠标位置归一化为设备坐标。x 和 y 方向的取值范围是 (-1 to +1)

        mouse.x = ( (event.clientX-canvas.offsetLeft) / 1000 ) * 2 - 1;
        mouse.y = - ( (event.clientY-canvas.offsetTop) / 618 ) * 2 + 1;
        raycaster.setFromCamera( mouse, camera );
        var intersects = raycaster.intersectObjects( scene.children );
        console.log(intersects)
        for(let item of intersects){


          if(item.object.id===zhushe.id){
            show("注射室","包括静脉注射、皮下注射、肌肉注射、局部封闭注射的操作流程，常见问题的处理方法，输液泵、加热垫的使用方法，注射室的消毒流程。")
            return
          }else if(item.object.id===zhenshi.id){
            show("诊室","包括诊室的布局介绍；对宠物进行临床基本检查（视、听、触、嗅等）、疾病诊断；与宠物主人交流并根据情况开具处方。")
            return
          }else if(item.object.id===yaofang.id){
            show("药房","包括对各种药物的存放要求、处方的审核流程、药物的发放流程、常见药物的使用说明等。")
            return
          }else if(item.object.id===chuzhi.id){
            show("处置室","包括口服投药、换药、清洗耳道、挤肛门腺、修剪指甲、鼻饲管放置、灌肠、安乐死等基本处置操作流程。")
            return
          }else if(item.object.id===mianyi.id){
            show("免疫室","包括为健康宠物接种疫苗的流程，对常见并发症的处理流程，对常见免疫相关问题的解答等。")
            return
          }else if(item.object.id===zhunbei.id){
            show("手术准备室","包括术前对宠物进行麻前给药、注射麻醉、吸入麻醉的流程，保定、剃毛、消毒的流程，常见手术器械的介绍，手术器械包的准备、灭菌流程，手术人员的消毒、穿戴手术衣流程等。")
            return
          }else if(item.object.id===huayan.id){
            show("化验室","包括对送检样本的预处理，对相应样本进行血常规、血液生化、电解质、血气、血凝指标、激素指标、尿常规、微生物学检查、药敏、皮肤刮片、粪便检查、传染病检查等检查操作流程。")
            return
          }else if(item.object.id===shoushu.id){
            show("手术室","包括手术室的布局介绍，手术室消毒流程，手术无菌要求，常规手术、特殊手等的操作规范。")
            return
          }else if(item.object.id===dangan.id){
            show("档案室","包括病例档案的合理保存与数据统计等。")
            return
          }else if(item.object.id===bingli.id){
            show("病例剖检室","包括对病死动物剖解的流程，病理剖检室的消毒流程，病历剖检过程的人员要求，病理剖检过程中的人道关怀。")
            return
          }else if(item.object.id===yingxiang.id){
            show("影像室","包括X线检查、B超检查以及CT、MRI检查。如X线检查：X光机的结构功能介绍、全身各部位的摆位、拍摄条件的选择、拍摄流程、洗片的操作流程。B超检查：扫查探头的选择、全身各个部位扫查的摆位、腹部扫查流程。")
            return
          }else if(item.object.id===zhuyuan.id){
            show("住院部","包括对需要住院的病例进行护理分级，不同护理级别的要求，住院部的工作流程，住院部的消毒流程等。")
            return
          }else if(item.object.id===zhuanke.id){
            show("专科检查室","包括对眼科、骨科、神经科、心脏科等专科疾病的检查，如眼科（检眼镜检查、眼压检查、裂隙灯检查、眼底检查、泪液分泌量检查等）、心脏科检查（心脏听诊、心电图检查等）、神经学检查（步态检查、各种反射检查等）等。")
            return
          }



        }

        textShow.style["display"] = "none"


      }

      window.addEventListener( 'click', onClick, false );


      // 渲染循环
      const animate = function () {
        // 通过摄像机和鼠标位置更新射线


        requestAnimationFrame( animate );
        renderer.render( scene, camera );
      };

      animate();
    }
  }
}
</script>

<style scoped>
.container{
  overflow: hidden;
}



#canvas{

  width: 1000px;
  height: 618px;
  position: relative;
  /*margin: 0 auto;*/
  margin: auto;
  margin-top: 23px;
  /*box-shadow:2px 2px 5px #000;*/
}
.text{
  position: absolute;
  width: 200px;
  /*height: 200px;*/
  background: rgba(1, 19, 67, 0.5);
  border: 2px solid #00a1ff;
  border-radius: 8px;
  left: 20px;
  top: 30px;
  display: none;

}
h3{
  color: blue;
  text-align: center;

}
.text p{
  color: orange;
}
</style>