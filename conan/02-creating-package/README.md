[conan.io/creating-package](https://docs.conan.io/en/latest/creating_packages/getting_started.html#creating-the-package-recipe)


# Execução

```
conan new Hello/0.1 -t
conan create . demo/testing

conan export . demo/testing
conan install Hello/0.1@demo/testing --build=Hello
conan test test_package Hello/0.1@demo/testing

conan create . demo/testing -s build_type=Debug
conan create . demo/testing -o Hello:shared=True -s arch=x86_64

```


nao precisa fazer git clone




# Dificuldades


## Problema 1

```
conan create . demo/testing -o Hello:shared=True -s arch=x86
```

### Log
In file included from /home/user/.conan/data/Hello/0.1/demo/testing/build/87fdf97cb701ccab39d07def20f53b2bc695cf6e/hello/hello.cpp:1:0:
/usr/include/c++/5/iostream:38:28: fatal error: bits/c++config.h: No such file or directory


### Solução

```
sudo apt-get install gcc-multilib g++-multilib
```
