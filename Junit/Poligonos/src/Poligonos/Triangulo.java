package Poligonos;

public class Triangulo extends Ponto2D {
	private Ponto2D p1 = new Ponto2D();
	private Ponto2D p2 = new Ponto2D();
	private Ponto2D p3 = new Ponto2D();
	private double a1,a2,a3;
	private String tipo;

	public Triangulo(){
		p1.setX(1);
		p1.setY(0);
		
		p2.setX(-1);
		p2.setY(0);
		
		p3.setX(0);
		p3.setY(1);
		
		this.classifica();
	}

	public Triangulo(Ponto2D p1, Ponto2D p2, Ponto2D p3){
		this.p1 = p1;
		this.p2 = p2;
		this.p3 = p3;
		
		this.a1 = DistPontos(p1,p2);
		this.a2 = DistPontos(p2,p3);
		this.a3 = DistPontos(p3,p1);
	}
	
	public Ponto2D getp1(){
		return p1; 
	}

	public Ponto2D getp2(){
		return p1; 
	}
	
	public Ponto2D getp3(){
		return p1; 
	}
	
	public double geta1() {
		return this.a1;
	}
	
	public double geta2() {
		return this.a2;
	}
	
	public double geta3() {
		return this.a3;
	}
	
	public String gettipo() {
		this.classifica();
		return this.tipo;
	}
	
	public void setp1(Ponto2D p1){
		this.p1 = p1; 
	}

	public void setp2(Ponto2D p2){
		this.p2 = p2; 
	}
	
	public void setp3(Ponto2D p3){
		this.p3 = p3;
	}
	
	public void classifica(){
		double a = this.a1, b = this.a2, c = this.a3;
		if( a <= 0 		|| b <= 0 		|| c <= 0	||
			a >= (b+c) 	|| b >= (a+c) 	|| c >= (b+a))
			this.tipo = "invalido";
		if(a==b && b==c)
			this.tipo = "equilatero";
		else if(a==b || b==c || a==c)
			this.tipo = "isosceles";
		else 
			this.tipo = "escaleno";
	}
}
