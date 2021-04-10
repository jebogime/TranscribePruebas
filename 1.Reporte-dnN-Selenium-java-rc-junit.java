package com.example.tests;

import com.thoughtworks.selenium.Selenium;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.WebDriver;
import com.thoughtworks.selenium.webdriven.WebDriverBackedSelenium;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;
import java.util.regex.Pattern;
import static org.apache.commons.lang3.StringUtils.join;

public class PaiwebReporteDnn {
	private Selenium selenium;

	@Before
	public void setUp() throws Exception {
		WebDriver driver = new ChromeDriver();
		String baseUrl = "https://www.blazedemo.com/";
		selenium = new WebDriverBackedSelenium(driver, baseUrl);
	}

	@Test
	public void testPaiwebReporteDnn() throws Exception {
		// Label: Test
		selenium.resizeWindow(1366,568);
		selenium.open("https://otranscribe.com/");
		selenium.click("css=span.start-ready");
		selenium.click("css=input[type=\"file\"]");
		selenium.type("css=input[type=\"file\"]", "C:\\fakepath\\error aprobacion control.mp4");
		selenium.click("css=div.button.play-pause");
	}

	@After
	public void tearDown() throws Exception {
		selenium.stop();
	}
}
