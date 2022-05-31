.source Program.java
.class public Program
.super java.lang.Object

.method public <init>()V
.var 0 is this LProgram; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
Label0:
	iconst_2
	istore_1
Label2:
	iload_1
	iconst_0
	if_icmplt Label3
	iload_1
	iconst_3
	if_icmpgt Label3
Label6:
	iload_1
	invokestatic io/putInt(I)V
Label7:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label3:
Label1:
	return
.limit stack 2
.limit locals 2
.end method
