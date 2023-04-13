package com.ravi.common;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class App{
    public static void main(String[] args){
        ApplicationContext context = new ClassPathXmlApplicationContext("Spring-M");
        HelloWorld obj = (HelloWorld) context.getBean("helloworld");
        obj.printHello();
    }
}