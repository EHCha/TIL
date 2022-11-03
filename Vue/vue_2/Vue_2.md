### Node.js

자바스크립트는 브라우저를 조작하는 유일한 언어이지만 브라우저 밖에서는 구동할수 없었다.

Until, Node.js의 등장 전까진



### Vue CLI

Vue 개발을 위한 표준 도구

프로젝트 구성을 도와주는 역할

확장 플러그인, GUI 등



설치 후

한단계 더 들어가서 서버 구동해야함 



### node_modules

node.js 환경의 여러 의존성 모듈



### node_modules-babel

JavaScript compiler

자바스크립트의 파편화, 표준화의 영향으로 작성된 코드의 스펙트럼이 매우 다양

​	최신 문법을 사용해도 브라우저 버전 별로 동작하지 않는 상황이 발생 (호환성 문제를 잡아주는 babel)



node_modules-Webpack



static module bundler

Bundler란

모듈간의 의존성 해결 위한 작업이 Bundling

이러한 일을 해주는 도구가 Bundler 이고, Webpack 은 다양한 Bundler 중 하나

모듈을 하나로 묶어 주고 묶인 파일은 하나로 만들어짐



SFC

HTML, CSS, JS를 Vue라는 확장자를 가진 파일 안에서 관리하며 개발



## Vue component

템플릿 HTML의 Body 부분

스크립트 JavaScript 코드가 작성 되는 곳 Vue 인스턴스 구성하는 대부분이 작성됨

스타일(CSS) CSS 가 작성되며 컴포넌트의 스타일을 담당





컴포넌트 등록 3단계

1. 불러오기

2. 등록하기

3. 보여주기



https://vue2.hphk.io/

싱글 컴포넌트 이름 규칙 지정 



데이터 유지 보수를 편한게 하기 위해

부모 => 자식으로 데이터의 흐름

pass props 방식



### Pass Prop:

요소의 속성을 사용하여 데이터 전달

props는 부모 컴포넌트의 정보 전달을 위한 사용자 지정 특성

정적인 데이터 전달시 static props 

prop-data-name="value"



자식 => 부모로 데이터의 흐름

emit event의 방식





emit with data

두번째 인자로 데이터 넣어줌 앞에는 이름

```vue
methods: {
    childToParent: function() {
      this.$emit('child-to-parent', '나는 자식이 보낸 데이터다')
    }
  },
```



 전달한 데이터는 이벤트와 연결된 부모 컴포넌트 핸들러 함수의 인자로 사용 가능



자식 컴포넌트에 있는 버튼 클릭 이벤트를 청취하여

연결된 핸들러 함수 (ChildToParent) 호출



호출된 함수에서 $emit을 통해 부모 컴포넌트에 이벤트를 발생

이벤트에 데이터를 함께 전달



부모 컴포넌트는 자식 컴포넌트의 이벤트 를 청취하여 연결된 핸들러 함수 호출



 HTML 요소에서 사용할 때는Kebab-case

JavaScript에서 사용할 때는 camelCase

### Props

상위 => 하위 흐름에서 HTML 요소로 내려줌: kebab-case

하위에서 받을 때 JavaScript에서 받음: camelCase

### Emit

emit 이벤트를 발생 시키면 HTML 요소가 이벤트를 청취함: kebab-case

메서드, 변수명 등은 JS에서 사용함 camelCase