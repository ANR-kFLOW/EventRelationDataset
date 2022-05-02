import org.apache.xerces.parsers.DOMParser;
import org.xml.sax.ErrorHandler;
import org.w3c.dom.Document;
import org.w3c.dom.Node;
import org.w3c.dom.Element;
import org.w3c.dom.NodeList;
import org.xml.sax.SAXException;
import org.xml.sax.SAXParseException;
import org.xml.sax.SAXNotRecognizedException;
import org.xml.sax.SAXNotSupportedException;
import java.io.*;
import java.util.*;

// A Valdating DOM Application with registered Error Handlers
public class ValidateTimeML implements ErrorHandler 
{
	public static String xmlFilename;

	// Constructor
	public ValidateTimeML () {
		//  Create a Xerces DOM Parser
		DOMParser parser = new DOMParser();

		//  Turn Validation on
		try {
			parser.setFeature("http://xml.org/sax/features/validation", true);
			parser.setFeature("http://apache.org/xml/features/validation/schema", true);
			parser.setFeature("http://apache.org/xml/features/validation/schema-full-checking", true);
		} catch (SAXNotRecognizedException e) {
			System.err.println (e);
		} catch (SAXNotSupportedException e) {
			System.err.println (e);
		}

		//  Register Error Handler
		parser.setErrorHandler (this);

		//  Parse the Document and traverse the DOM
		try {
			parser.parse(xmlFilename);
			// Document document = parser.getDocument();
			// traverse (document);
		} catch (SAXException e) {
			System.err.println (e);
		} catch (IOException e) {
			System.err.println (e);
		} catch (Exception e) {
			System.err.println (e);
		}
	}

	// Traverse DOM Tree. Print out Element Names
	private void traverse (Node node) {
		int type = node.getNodeType();
		if (type == Node.ELEMENT_NODE)
			System.out.println (node.getNodeName());
		NodeList children = node.getChildNodes();
		if (children != null) {
			for (int i=0; i< children.getLength(); i++)
				traverse (children.item(i));
		}
	}
	
	// Warning Event Handler
	public void warning (SAXParseException e) throws SAXException {
		System.err.println ("Warning: "+e);
	}
	
	// Error Event Handler
	public void error (SAXParseException e) throws SAXException {
		System.err.println ("Error: "+e);
	}

	// Fatal Error Event Handler
	public void fatalError (SAXParseException e) throws SAXException {
		System.err.println ("Fatal Error: "+e);
	}

	// Main Method
	public static void main (String[] args) {

		File dir = new File (args[0]);
		try {
			System.setErr (new PrintStream (new FileOutputStream (args[1] )));
		} catch (FileNotFoundException e) {
			System.err.println (e);
		}

		if (dir.isDirectory()) {
			String[] dirList = dir.list ( );
			int fileCounter = 0;
			System.out.println("\nValidating files in " + dir + "\n");
			for ( int i = 0 ; i < dirList.length ; i++ ) {
				if ( dirList[i].endsWith (".tml" ) ) {
					fileCounter++;
					xmlFilename = args[0].concat("/").concat(dirList[i]);
					System.err.println("\n"+dirList[i]+"\n");
					System.out.println("  "+dirList[i]);
					ValidateTimeML validatingDOM = new ValidateTimeML ();
					//if (fileCounter == 10) break;
				}
			}
		} else if (dir.isFile()) {
			xmlFilename = dir.toString();
			System.err.println("\n"+xmlFilename+"\n");
			System.out.println("\nValidating "+xmlFilename);
			ValidateTimeML validatingDOM = new ValidateTimeML ();
		} else {
			System.out.println("\nError, no valid input file or directory.");
			System.out.println("\nUsage:\n\n\tjava ValidateTimeML <DIR_OR_FILE> <ERROR_FILE>");
		}
		System.out.println();
	}
}

