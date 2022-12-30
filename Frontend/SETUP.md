# Flutter 설정법

1. https://docs.flutter.dev/get-started/install 에 들어가서 적힌 설명대로 셋업해준다.
2. `cd` 명령어를 이용해 `Frontend/fild_my_pill` 폴더 안에 들어와서 `flutter doctor` 명령어를 쳤을때 `No issues found!` 가 뜰 수 있을정도로 셋업해준다.
3. 해당 위치에서 `flutter run` 을 치면 프로젝트가 실행 된다.
4. 안드로이드 스튜디오에서 `Virtual Device Manager` 창을 열어서 안드로이드 가상기계를 킬 수 있다. 이후 `flutter run` 을 실행하면 안드로이드 가상기계로 실행시킬수 있는 옵션이 활성화 된다.
5. 맥에서는 필요한 Xcode 설치를 전부 충족한 다음, `open -a Simulator` 를 통해 아이폰 가상기계를 킬 수 있다. 이후 `flutter run` 을 실행하면 애플 가상기계로 실행시킬수 있는 옵션이 활성화 된다.(Mac OS 만 가능)
6. 이 외에도 윈도우에서는 Window 창, 맥북에서는 MacOS 창, 브라우저로는 크롬등으로 실행시킬수 있다.