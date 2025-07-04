using System;
using System.Collections.Generic;

public class BrowserHistory
{
	private readonly Stack<string> _forwards = [];
	private readonly Stack<string> _backwards = [];

	public BrowserHistory(string homepage)
	{
		_forwards.Push(homepage);
	}

	public void Visit(string url)
	{
		if (_backwards.Count > 0)
		{
			_backwards.Clear();
		}

		_forwards.Push(url);
	}

	public string Back(int steps)
	{
		while (_forwards.Count > 1 && steps != 0)
		{
			_backwards.Push(_forwards.Pop());
			steps -= 1;
		}

		return _forwards.Peek();
	}

	public string Forward(int steps)
	{
		while (_backwards.Count > 0 && steps != 0)
		{
			_forwards.Push(_backwards.Pop());
			steps -= 1;
		}

		return _forwards.Peek();
	}
}


public class Program
{
	private static void Visit(BrowserHistory browser, string url)
	{
		Console.WriteLine($"Visit {url}");
		browser.Visit(url);
	}

	private static void Back(BrowserHistory browser, int steps)
	{
		Console.WriteLine($"Back {browser.Back(steps)}");
	}

	private static void Forward(BrowserHistory browser, int steps)
	{
		Console.WriteLine($"Back {browser.Forward(steps)}");
	}

	public static void Main()
	{
        Console.WriteLine("1472. Design Browser History")

		BrowserHistory browser = new("leetcode");
		
        Visit(browser, "google");
		Visit(browser, "facebook");
		Visit(browser, "youtube");
		Back(browser, 1);
		Back(browser, 1);
		Forward(browser, 1);
		Visit(browser, "linkedin");
		Forward(browser, 2);
		Back(browser, 2);
		Back(browser, 7);
	}
}