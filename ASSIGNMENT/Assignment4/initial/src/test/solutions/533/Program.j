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
Label0:
	iconst_5
	invokestatic io/putInt(I)V
	ldc 5.67
	invokestatic io/putFloat(F)V
	ldc "abc"
	invokestatic io/putString(Ljava/lang/String;)V
Label1:
	return
.limit stack 2
.limit locals 1
.end method
