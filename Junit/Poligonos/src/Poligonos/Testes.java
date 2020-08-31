package Poligonos;
import org.junit.*;
import static org.junit.Assert.assertThat;
import static org.hamcrest.CoreMatchers.*;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.Test;
class Testes {
	@Test
	void test() {
		//construtor padrao Triangulo
		//instancia um triangulo equilatero, (1,0),(-1,0),(0,1)
		Triangulo t = new Triangulo();
		// o triangulo criado por padrão não é invalido.
		assertThat(t.gettipo(),is(not("invalido")));
		// o triangulo criado por padrão é equilatero
		assertThat(t.gettipo(),is("equilatero"));
	}
}