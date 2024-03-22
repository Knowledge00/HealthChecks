import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.By;

public class webtable1 {

    public static void main(String[] args) {

        System.setProperty("webdriver.chrome", "C:\\Users\\zainr\\Downloads\\chromedriver_win32\\chromedriver.exe");
        WebDriver driver =new ChromeDriver();

        driver.get("https://riskscore.diabetes.org.uk/start");
        int r=driver.findElement(new By.xpath("start-survey")).click();
        system.out.println(r);




    }


}